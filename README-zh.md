# Spark Docker 集群

# 快速启动

使用前, 请设置 docker 加速器

```
# 启动集群
docker-compose down && docker-compose up -d

# 执行 python 任务: ./data/spark-apps/test.py
chmod +x crimes-app.sh
./crimes-app.sh

# 执行 collect_log.py
chmod +x crimes-app-collect-log.sh
./crimes-app-collect-log.sh

# 浏览器访问 http://localhost:8080 以查看集群信息

```
