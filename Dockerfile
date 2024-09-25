
FROM python:3.9


WORKDIR /code

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV PATH="/opt/venv/bin:$PATH"

COPY ./app /code/app

RUN mkdir -p /code/app/files

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]