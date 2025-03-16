# 使用官方輕量級的 Node.js 映像檔
FROM python:3.9

# 設定工作目錄
WORKDIR /app

# 複製 package.json 和 package-lock.json（如果有）
COPY . /app

# 安裝相依套件
RUN pip install -r requirements.txt
# 複製專案檔案

# 啟動應用程式
CMD ["python", "main.py"]