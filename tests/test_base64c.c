#include <stdio.h>
#include <string.h>
#include <time.h>
#include <assert.h>
#include "base64c.h"

#define TEST_CASES 6
#define LARGE_SIZE 1000000
#define BENCHMARK_ITERATIONS 1000

// Test cases
const char* test_strings[TEST_CASES] = {
    "",
    "f",
    "fo",
    "foo",
    "foob",
    "fooba",
};

const char* expected_standard[TEST_CASES] = {
    "",
    "Zg==",
    "Zm8=",
    "Zm9v",
    "Zm9vYg==",
    "Zm9vYmE=",
};

const char* expected_urlsafe[TEST_CASES] = {
    "",
    "Zg==",
    "Zm8=",
    "Zm9v",
    "Zm9vYg==",
    "Zm9vYmE=",
};

void test_encoding() {
    printf("Testing encoding...\n");
    for (int i = 0; i < TEST_CASES; i++) {
        PyObject* args = Py_BuildValue("y#", test_strings[i], strlen(test_strings[i]));
        PyObject* result = b64encode(NULL, args);
        assert(result != NULL);
        
        const char* encoded = PyBytes_AsString(result);
        assert(encoded != NULL);
        
        printf("Input: %s\n", test_strings[i]);
        printf("Encoded: %s\n", encoded);
        printf("Expected: %s\n", expected_standard[i]);
        assert(strcmp(encoded, expected_standard[i]) == 0);
        
        Py_DECREF(result);
        Py_DECREF(args);
    }
    printf("Encoding tests passed.\n\n");
}

void test_decoding() {
    printf("Testing decoding...\n");
    for (int i = 0; i < TEST_CASES; i++) {
        PyObject* args = Py_BuildValue("y#", expected_standard[i], strlen(expected_standard[i]));
        PyObject* result = b64decode(NULL, args);
        assert(result != NULL);
        
        const char* decoded = PyBytes_AsString(result);
        assert(decoded != NULL);
        
        printf("Input: %s\n", expected_standard[i]);
        printf("Decoded: %s\n", decoded);
        printf("Expected: %s\n", test_strings[i]);
        assert(strcmp(decoded, test_strings[i]) == 0);
        
        Py_DECREF(result);
        Py_DECREF(args);
    }
    printf("Decoding tests passed.\n\n");
}

void test_urlsafe() {
    printf("Testing URL-safe encoding and decoding...\n");
    for (int i = 0; i < TEST_CASES; i++) {
        PyObject* args = Py_BuildValue("y#", test_strings[i], strlen(test_strings[i]));
        PyObject* encoded = urlsafe_b64encode(NULL, args);
        assert(encoded != NULL);
        
        const char* encoded_str = PyBytes_AsString(encoded);
        assert(encoded_str != NULL);
        
        printf("Input: %s\n", test_strings[i]);
        printf("URL-safe encoded: %s\n", encoded_str);
        printf("Expected: %s\n", expected_urlsafe[i]);
        assert(strcmp(encoded_str, expected_urlsafe[i]) == 0);
        
        PyObject* decoded = urlsafe_b64decode(NULL, Py_BuildValue("y#", encoded_str, strlen(encoded_str)));
        assert(decoded != NULL);
        
        const char* decoded_str = PyBytes_AsString(decoded);
        assert(decoded_str != NULL);
        
        printf("Decoded: %s\n", decoded_str);
        assert(strcmp(decoded_str, test_strings[i]) == 0);
        
        Py_DECREF(encoded);
        Py_DECREF(decoded);
        Py_DECREF(args);
    }
    printf("URL-safe tests passed.\n\n");
}

void benchmark() {
    printf("Running benchmarks...\n");
    char* large_input = malloc(LARGE_SIZE);
    memset(large_input, 'A', LARGE_SIZE);
    
    PyObject* args = Py_BuildValue("y#", large_input, LARGE_SIZE);
    
    clock_t start, end;
    double cpu_time_used;
    
    // Benchmark encoding
    start = clock();
    for (int i = 0; i < BENCHMARK_ITERATIONS; i++) {
        PyObject* result = b64encode(NULL, args);
        Py_DECREF(result);
    }
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Encoding %d times took %f seconds\n", BENCHMARK_ITERATIONS, cpu_time_used);
    
    // Benchmark decoding
    PyObject* encoded = b64encode(NULL, args);
    PyObject* decode_args = Py_BuildValue("y#", PyBytes_AsString(encoded), PyBytes_Size(encoded));
    
    start = clock();
    for (int i = 0; i < BENCHMARK_ITERATIONS; i++) {
        PyObject* result = b64decode(NULL, decode_args);
        Py_DECREF(result);
    }
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Decoding %d times took %f seconds\n", BENCHMARK_ITERATIONS, cpu_time_used);
    
    Py_DECREF(encoded);
    Py_DECREF(decode_args);
    Py_DECREF(args);
    free(large_input);
    
    printf("Benchmarks completed.\n");
}

int main() {
    // Initialize Python
    Py_Initialize();
    
    // Run tests
    test_encoding();
    test_decoding();
    test_urlsafe();
    
    // Run benchmarks
    benchmark();
    
    // Finalize Python
    Py_Finalize();
    
    printf("All tests passed successfully.\n");
    return 0;
}