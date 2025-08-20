FROM python:3.12-slim
COPY req.txt req.txt
RUN pip install -r req.txt
COPY app.py app.py
CMD ["flask", "--app", "app", "run", "-h", "0.0.0.0"]