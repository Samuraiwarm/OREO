FROM python:3.6-alpine
WORKDIR /app
COPY oreo.py /oreo.py
RUN chmod +x /oreo.py
CMD ["python3","/oreo.py"]
