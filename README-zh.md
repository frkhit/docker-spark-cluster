# Spark Docker 集群

# 快速启动

使用前, 请设置 docker 加速器

```
# 启动集群
docker-compose down && docker-compose up -d

# 执行 python 任务: ./data/spark-apps/test.py
./crimes-app.sh

# 浏览器访问 http://localhost:8080 以查看集群信息

```
