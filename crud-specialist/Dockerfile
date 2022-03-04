FROM debian:stable-slim

RUN apt-get update
RUN apt-get install fortune default-mysql-client -y

COPY ./app.sh /usr/bin/app.sh
RUN chmod +x /usr/bin/app.sh

CMD ["app.sh"]