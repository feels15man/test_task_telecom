FROM ubuntu:22.04

RUN apt update && apt install python3 python3-pip -y && \
    pip3 install requests && rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

WORKDIR /app

COPY task_1/script.py .

CMD ["python3", "script.py"]