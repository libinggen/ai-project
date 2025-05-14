FROM python:3.11-slim

WORKDIR /app

# 拷贝依赖文件并安装
COPY requirements.txt .
COPY requirements-extension.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-extension.txt

# 拷贝 app 代码（只复制 app 目录）
COPY app ./app

# 设置默认启动命令（主模块是 app/main.py）
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
