FROM python:3.6

WORKDIR /code/main

COPY ./main/requirements.txt /code/main/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/main/requirements.txt
RUN pip install fastapi uvicorn urlopen
RUN pip install requests

COPY ./ /code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]