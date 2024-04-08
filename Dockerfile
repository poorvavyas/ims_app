FROM python

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .

EXPOSE 8080

# copy docker-entrypoint.sh
COPY ./django.sh .

ENTRYPOINT ["./django.sh"]


