# coding:utf-8

__author__ = 'rk.feng'

from pyspark import SparkContext, SparkConf

conf = SparkConf().set("spark.worker.cleanup.enabled", False)
sc = SparkContext(
    master="spark://spark-master:7077",
    appName="WordCount",
    environment={"PYSPARK_PYTHON": "python3"},
    conf=conf
)
lines = sc.textFile("/spark/README.md")
print("count of text is {}".format(lines.count()))
result = lines.flatMap(lambda x: x.split(" ")).countByValue()
for key, value in result.items():
    print("%s %i" % (key, value))
