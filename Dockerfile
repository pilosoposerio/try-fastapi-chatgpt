FROM python:3.8-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./try_fastapi_chatgpt /app/try_fastapi_chatgpt

CMD ["uvicorn", "try_fastapi_chatgpt.application.api.fastapi:app", "--host", "0.0.0.0", "--port", "3000"]