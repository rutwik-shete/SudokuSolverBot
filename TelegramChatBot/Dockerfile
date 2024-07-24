FROM pytorch/pytorch

WORKDIR /sudoku-telebot

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./app/* ./app/

CMD ["python3","app/main.py"]