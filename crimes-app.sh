#!/bin/bash

docker run --rm --network docker-spark-cluster_spark-network -v `pwd`/data/spark-apps:/opt/spark-apps --env PYSPARK_PYTHON=python3 frkhit/docker-spark-cluster-submit:latest /spark/bin/spark-submit /opt/spark-apps/test.py
