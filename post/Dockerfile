FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt  \
    && pip install pydantic[email]

COPY . .

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8001"]
