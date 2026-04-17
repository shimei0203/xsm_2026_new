# 基础镜像#Basic image
FROM ubuntu:22.04

# 设置环境变量，避免交互式安装弹窗#Set environment variables to avoid interactive installation pop ups

ENV TZ=Asia/Shanghai
ENV DEBIAN_FRONTEND=noninteractive

# 1. 安装系统级依赖# 1. Install system level dependencies

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    unzip \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    liblzma-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2. 编译安装 Python 3.8.10 (使用清华源加速)# 2. Compile and install Python 3.8.10 (using Tsinghua Source Acceleration)

RUN wget --no-check-certificate https://mirrors.tuna.tsinghua.edu.cn/python/3.8.10/Python-3.8.10.tgz \
    && tar -xf Python-3.8.10.tgz \
    && cd Python-3.8.10 \
    && ./configure --enable-optimizations \
    && make -j$(nproc) \
    && make altinstall \
    && cd .. \
    && rm -rf Python-3.8.10 Python-3.8.10.tgz

# 3. 配置 Python 软链接# 3. Configure Python soft links

RUN update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.8 1 \
    && update-alternatives --install /usr/bin/pip3 pip3 /usr/local/bin/pip3.8 1

# 4. 设置工作目录# 4. Set working directory

WORKDIR /app

# 5. 复制并解压项目文件# 5. Copy and extract project files

COPY shimei_assessment.zip /app/
RUN unzip -o /app/shimei_assessment.zip -d /app/ \
    && rm /app/shimei_assessment.zip

# 6. 赋予脚本执行权限# 6. Granting script execution permissions

RUN chmod +x /app/csv-cleaner-cli/tests/test.sh

# 7. 【关键】预创建输出目录# 7. 【 Key 】 Pre create output directory

# 虽然运行时会挂载，但在 Dockerfile 里先建好目录是个好习惯，防止权限问题#Although it will be mounted at runtime, it is a good habit to first create a directory in Dockerfile to prevent permission issues

RUN mkdir -p /output

# 8. 启动命令# 8. startup command

# 这里逻辑是：先执行脚本，然后把生成的文件复制到挂载点#The logic here is: first execute the script, and then copy the generated file to the mount point

CMD ["sh", "-c", "\
    echo '🚀 开始执行数据清洗...' && \
    cd /app/csv-cleaner-cli/ && \
    ./tests/test.sh && \
    echo '📂 正在导出文件...' && \
    cp /app/csv-cleaner-cli/clean_data.csv /output/ && \
    echo '✅ 成功！文件已保存至 /output/clean_data.csv' \
    "]