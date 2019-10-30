FROM python:3

RUN git clone https://github.com/JJHernandez99/2019-parcial-3

WORKDIR /2019-parcial-3/58160-HERNANDEZ-JOAQUIN

RUN pip freeze > requirements.txt

RUN pip install requests

RUN pip install -r requirements.txt

CMD ["python", "./tateti.py"]