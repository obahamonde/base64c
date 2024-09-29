FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry install --no-root --no-dev

CMD ["pytest", "--html=test_report.html"]	





