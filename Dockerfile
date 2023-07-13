FROM python:3.9

WORKDIR /deteccao-faces/HOG.pydo

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "deteccao-faces/HOG.py"]

 