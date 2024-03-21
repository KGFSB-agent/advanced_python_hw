FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt install -y python3 python3-pip texlive-full && \
    pip install --upgrade pip && \
    pip install poetry

WORKDIR /project

COPY poetry.lock .
COPY pyproject.toml .
COPY tasks/task_2_2_2.py .
COPY artifacts/arifacts_task_2_2/Mr_Svin.png artifacts/arifacts_task_2_2/

RUN poetry install 

CMD ["poetry", "run", "python", "task_2_2_2.py"]
