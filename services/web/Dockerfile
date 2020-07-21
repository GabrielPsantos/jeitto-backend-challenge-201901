#baseImage
FROM python:3.8.0-alpine

#Set work dir
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

# install pyscopg2 dependencies
RUN apk update \
        && apk add postgresql-dev gcc python3-dev musl-dev

#install Dependencies

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

#copyproject
COPY . /usr/src/app

#run entrypoint.sh
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
