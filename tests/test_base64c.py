import base64c
import base64
import time
import os
import pytest
import random
from typing import Callable, List, Tuple, Dict
import json
from string import ascii_letters, digits

# Helper functions
def random_text(length: int) -> bytes:
    return "".join(random.choice(ascii_letters + digits) for _ in range(length)).encode()

def random_binary(length: int) -> bytes:
    return os.urandom(length)

def generate_test_data() -> List[Tuple[str, bytes]]:
    return [
        ("Small text", random_text(100)),
        ("Large text", random_text(1000000)),
        ("Binary data", random_binary(1000000)),
        ("JPEG image", open("assets/sample.jpeg", "rb").read()),
        ("PNG image", open("assets/sample.png", "rb").read()),
        ("MP3 audio", open("assets/sample.mp3", "rb").read()),
    ]

def benchmark(func: Callable, data: bytes, iterations: int = 100) -> float:
    start = time.time()
    for _ in range(iterations):
        func(data)
    end = time.time()
    return end - start

# Test data fixture
@pytest.fixture(scope="module")
def test_data():
    return generate_test_data()

# Fixture to store results
@pytest.fixture(scope="module")
def performance_results():
    return {}

# Correctness tests
@pytest.mark.parametrize(
    "func_name",
    [
        "b64encode", "b64decode",
        "standard_b64encode", "standard_b64decode",
        "urlsafe_b64encode", "urlsafe_b64decode",
    ],
)
def test_correctness(func_name, test_data):
    for name, data in test_data:
        stdlib_func = getattr(base64, func_name)
        base64c_func = getattr(base64c, func_name)

        if "decode" in func_name:
            data = getattr(base64, func_name.replace("decode", "encode"))(data)

        stdlib_result = stdlib_func(data)
        base64c_result = base64c_func(data)

        assert stdlib_result == base64c_result, f"{func_name} failed for {name}"

# Performance tests
@pytest.mark.parametrize(
    "func_name",
    [
        "b64encode", "b64decode",
        "standard_b64encode", "standard_b64decode",
        "urlsafe_b64encode", "urlsafe_b64decode",
    ],
)
def test_performance(func_name, test_data, performance_results):
    for name, data in test_data:
        stdlib_func = getattr(base64, func_name)
        base64c_func = getattr(base64c, func_name)

        if "decode" in func_name:
            data = getattr(base64, func_name.replace("decode", "encode"))(data)

        # Adjust iterations for large data
        iterations = 10 if len(data) > 100000 else 100

        stdlib_time = benchmark(stdlib_func, data, iterations)
        base64c_time = benchmark(base64c_func, data, iterations)
        speedup = stdlib_time / base64c_time

        # Store results in the performance_results fixture
        if name not in performance_results:
            performance_results[name] = {}
        performance_results[name][func_name] = {
            "stdlib_time": stdlib_time,
            "base64c_time": base64c_time,
            "speedup": speedup,
        }

        assert speedup > 1, f"{func_name} with {name} is not faster than stdlib"

# Pytest hook to generate the HTML report
def pytest_sessionfinish(session, exitstatus):
    results = session.config._performance_results

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>base64c Benchmark Performance Report</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
            .chart-container { width: 80%; margin: 20px auto; }
            table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            tr:nth-child(even) { background-color: #f9f9f9; }
            h1, h2 { text-align: center; }
        </style>
    </head>
    <body>
        <h1>base64c Benchmark Performance Report</h1>
        
        <h2>Summary Table</h2>
        <div id="summary">
            <table>
                <tr>
                    <th>Data Type</th>
                    <th>Function</th>
                    <th>Standard Library Time (s)</th>
                    <th>base64c Time (s)</th>
                    <th>Speedup (x)</th>
                </tr>
    """
    # Add rows to the summary table
    for data_type, result in results.items():
        for func_name, metrics in result.items():
            html_content += f"""
                <tr>
                    <td>{data_type}</td>
                    <td>{func_name}</td>
                    <td>{metrics['stdlib_time']:.6f}</td>
                    <td>{metrics['base64c_time']:.6f}</td>
                    <td>{metrics['speedup']:.2f}x</td>
                </tr>
            """
    html_content += """
            </table>
        </div>
        
        <h2>Performance Chart</h2>
        <div class="chart-container">
            <canvas id="speedupChart"></canvas>
        </div>
        
        <script>
            const results = RESULTS_PLACEHOLDER;

            // Data preparation for the chart
            const labels = Object.keys(results);
            const datasets = [];

            for (const [dataType, functions] of Object.entries(results)) {
                for (const [funcName, data] of Object.entries(functions)) {
                    let dataset = datasets.find(d => d.label === funcName);
                    if (!dataset) {
                        dataset = {
                            label: funcName,
                            data: [],
                            backgroundColor: `hsl(${datasets.length * 60}, 70%, 60%)`
                        };
                        datasets.push(dataset);
                    }
                    dataset.data.push(data.speedup);
                }
            }

            // Create speedup chart
            new Chart(document.getElementById('speedupChart'), {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: datasets
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Speedup (x times faster)'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'base64c Speedup by Function and Data Type'
                        },
                        legend: {
                            position: 'top',
                        }
                    }
                }
            });
        </script>
    </body>
    </html>
    """
    # Replace the placeholder with the actual results in JSON format
    html_content = html_content.replace("RESULTS_PLACEHOLDER", json.dumps(results))

    # Save the HTML report to the output directory
    os.makedirs('output', exist_ok=True)
    with open("output/benchmark_report.html", "w") as f:
        f.write(html_content)

# pytest hook to save performance results
def pytest_configure(config):
    config._performance_results = {}

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    results = session.config._performance_results
    if results:
        generate_html_report(results)


def generate_html_report(results: Dict):
    # Start the HTML content with basic structure and styling
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>base64c Benchmark Performance Report</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
            .chart-container { width: 80%; margin: 20px auto; }
            table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            tr:nth-child(even) { background-color: #f9f9f9; }
            h1, h2 { text-align: center; }
        </style>
    </head>
    <body>
        <h1>base64c Benchmark Performance Report</h1>
        
        <h2>Summary Table</h2>
        <div id="summary">
            <table>
                <tr>
                    <th>Data Type</th>
                    <th>Function</th>
                    <th>Standard Library Time (s)</th>
                    <th>base64c Time (s)</th>
                    <th>Speedup (x)</th>
                </tr>
    """

    # 3. **Generate the Table Rows**
    # - Iterate over the `results` dictionary to extract data and create rows in the HTML table
    for data_type, result in results.items():
        for func_name, metrics in result.items():
            html_content += f"""
                <tr>
                    <td>{data_type}</td>
                    <td>{func_name}</td>
                    <td>{metrics['stdlib_time']:.6f}</td>
                    <td>{metrics['base64c_time']:.6f}</td>
                    <td>{metrics['speedup']:.2f}x</td>
                </tr>
            """

    # 4. **Complete the Table and Add a Chart Container**
    # - Close the table and add a container for the chart that will be rendered using Chart.js
    html_content += """
            </table>
        </div>
        
        <h2>Performance Chart</h2>
        <div class="chart-container">
            <canvas id="speedupChart"></canvas>
        </div>
        
        <script>
            const results = RESULTS_PLACEHOLDER;

            // Data preparation for the chart
            const labels = Object.keys(results);
            const datasets = [];

            for (const [dataType, functions] of Object.entries(results)) {
                for (const [funcName, data] of Object.entries(functions)) {
                    let dataset = datasets.find(d => d.label === funcName);
                    if (!dataset) {
                        dataset = {
                            label: funcName,
                            data: [],
                            backgroundColor: `hsl(${datasets.length * 60}, 70%, 60%)`
                        };
                        datasets.push(dataset);
                    }
                    dataset.data.push(data.speedup);
                }
            }

            // Create the chart using Chart.js
            new Chart(document.getElementById('speedupChart'), {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: datasets
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Speedup (x times faster)'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'base64c Speedup by Function and Data Type'
                        },
                        legend: {
                            position: 'top',
                        }
                    }
                }
            });
        </script>
    </body>
    </html>
    """

    # 5. **Insert the Results Data into the Script**
    # - Convert the `results` dictionary to a JSON string and inject it into the `html_content`
    html_content = html_content.replace("RESULTS_PLACEHOLDER", json.dumps(results))

    # 6. **Save the HTML Report**
    # - Create an output directory if it doesn't exist and save the HTML content to a file
    with open("benchmark_report.html", "w") as f:
        f.write(html_content)