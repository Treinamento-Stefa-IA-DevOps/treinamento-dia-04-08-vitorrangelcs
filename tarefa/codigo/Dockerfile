#FROM python:3.8-slim
FROM python:3.8-slim

COPY . /tarefa
COPY requirements .

WORKDIR /tarefa

RUN pip install -r requirements

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80", "--reload"]
