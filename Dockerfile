FROM python:3.11

RUN apt update && \
    apt install locales firefox-esr -y &&\
    sed -i -e 's/# fr_FR.UTF-8 UTF-8/fr_FR.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales &&\
    apt clean


WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV TZ="Europe/Paris"
ENV LANG fr_FR.UTF-8
ENV LC_ALL fr_FR.UTF-8
ENV USE_FIREFOX true

CMD ["waitress-serve", "app:app"] 