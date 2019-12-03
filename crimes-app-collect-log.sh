#!/bin/bash

docker run --rm --network docker-spark-cluster_spark-network -v `pwd`/data/spark-apps:/opt/spark-apps -v `pwd`/data/spark-data:/opt/spark-data --env PYSPARK_PYTHON=python3 frkhit/docker-spark-cluster-submit:latest /spark/bin/spark-submit --conf spark.metrics.conf='/opt/spark-data/metrics.properties' /opt/spark-apps/collect_log.py
