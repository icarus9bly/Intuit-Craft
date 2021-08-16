FROM nginx:1.15.12-alpine

RUN mkdir /usr/share/nginx/static
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d
COPY ./snakes_and_ladders/static /usr/share/nginx/static

#Usage: docker build -t snl_nginx:latest -f nginx/Dockerfile .