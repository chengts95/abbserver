FROM python:3.5.2-alpine

MAINTAINER Cheng Tianshi <213132955@seu.edu.cn>

USER root
ADD /src /srv/
ADD requirements.txt /srv
RUN cd /srv \
	&& apk add --no-cache --virtual .build-deps  \
		bzip2-dev \
		gcc \
		libc-dev \
		linux-headers \
		make \
		ncurses-dev \
		openssl-dev \
		pax-utils \
		readline-dev \
		sqlite-dev \
		zlib-dev \
	&& pip3 install -U pip \
    && pip3 install -r requirements.txt \
	&& apk del .build-deps
WORKDIR /srv/web
RUN   ls -a
EXPOSE 8000

CMD ["python3", "/srv/web/restful.py"]

