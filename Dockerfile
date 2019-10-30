FROM python:3

RUN git clone https://github.com/valefaraz/2019-UltimoParcial.git

WORKDIR /2019-UltimoParcial

RUN pip freeze > requirements.txt

RUN pip3 install requests

RUN pip install parameterized

RUN pip install -r requirements.txt

CMD ["python", "./test_tateti.py"]
