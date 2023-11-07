FROM nginx:alpine

WORKDIR /var/www/html

COPY ./front-end/build .

COPY ./nginx.conf /etc/nginx/conf.d/default.conf