FROM node:latest

WORKDIR /app

COPY app/package.json app/package-lock.json ./
RUN npm install

COPY /app .

CMD ["npm", "start"]
