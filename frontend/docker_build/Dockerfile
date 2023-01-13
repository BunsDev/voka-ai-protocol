FROM nginx:latest

COPY frontend/dist /dist
COPY frontend/docker_build/nginx.conf /nginx.conf

RUN cat /nginx.conf > /etc/nginx/nginx.conf
