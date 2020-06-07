# Stage 1 - the build process
FROM node:14.4-stretch as frontend-build

WORKDIR /usr/src/app

COPY my-app/package.json my-app/yarn.lock ./

RUN yarn

COPY my-app/ ./

RUN yarn build

# Stage 2 - the production environment
FROM nginx:1.19-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=frontend-build /usr/src/app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
