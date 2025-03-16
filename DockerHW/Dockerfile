# 使用官方輕量級的 Node.js 映像檔
FROM node:20-alpine

# 設定工作目錄
WORKDIR /app

# 複製 package.json 和 package-lock.json（如果有）
COPY package*.json ./

# 安裝相依套件
RUN npm install

# 複製專案檔案
COPY . .

# 暴露應用程式埠
EXPOSE 3000

# 啟動應用程式
CMD ["npm", "start"]
