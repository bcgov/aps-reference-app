FROM node:latest as BUILD

WORKDIR /var/local

COPY package*.json .
RUN npm i

COPY . .
RUN npm run build

## Runtime Image
FROM nginx:stable

COPY --from=BUILD /var/local/dist/ /usr/share/nginx/html
COPY .dockerfile/nginx.conf /etc/nginx/nginx.conf
