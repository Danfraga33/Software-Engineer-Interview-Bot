FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

EXPOSE 5175

CMD ["npx", "vite", "preview", "--host", "0.0.0.0", "--port", "5175"]