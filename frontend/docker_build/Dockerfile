FROM nginx:latest

RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY frontend/dist /dist
COPY frontend/docker_build/nginx.conf /etc/nginx

