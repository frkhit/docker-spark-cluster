# coding:utf-8

__author__ = 'rk.feng'

import functools
import time

from pyspark import SparkContext, SparkConf


def log_wrapper(func):

    @functools.wraps(func)
    def wrapper(*args, **kw):
        log_str_list = []

        # before
        log_str_list.append("Logging before: {}".format(func.__name__))
        print(log_str_list[-1])
        _time_start = time.time()
        
        # do
        result = func(*args, **kw)
        log_str_list.append(result)
        
        # after
        log_str_list.append("Logging after: exec {}, time cost {:.2f}s!".format(func.__name__, time.time() - _time_start))
        print(log_str_list[-1])

        return "\n".join(log_str_list)

    return wrapper


@log_wrapper
def do_some_job(_line):
    # do some thine
    time.sleep(2)

    # create logger
    log_info = "I Got line: {}!".format(_line)
    print("Cannot show: {}".format(log_info))
    return log_info

conf = SparkConf().set("spark.worker.cleanup.enabled", False)
sc = SparkContext(
    master="spark://spark-master:7077",
    appName="CollectLogTest",
    environment={"PYSPARK_PYTHON": "python3"},
    conf=conf
)

line_list = [ "LINE {}".format(i) for i in range(20)]
new_pipe_rdd = sc.parallelize(line_list, len(line_list))

result_rdd = new_pipe_rdd.map(lambda v:do_some_job(v))

# do job
result_list = result_rdd.collect()

# print result
print("Result of spark is:\n{}".format("\n".join(result_list)))
