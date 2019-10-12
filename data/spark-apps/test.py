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
word_count_pair_list = [(key, value) for key, value in result.items()]
sorted_word_count_pair_list = sorted(word_count_pair_list, key=lambda x: x[1], reverse=True)
for (word, count) in sorted_word_count_pair_list:
    print("{}\t{}".format(word, count))

