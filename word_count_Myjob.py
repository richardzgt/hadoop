# -*- coding: utf-8 -*-
from mrjob.job import MRJob

class MRWordCounter(MRJob):
	"""docstring for MRWordCounter"""
	# mapper 函数接收每一行的输入数据，处理后返回一对key:value，
	# 初始化value数据为1；reducer接收mapper输出的key-value对进行整合，
	# 把相同key的value作累加(sum)操作后输出
	def mapper(self,key,line):
		for word in line.split():
			yield word , 1

	def reducer(self,word,occurrences):
		yield word,sum(occurrences)

if __name__ == '__main__':
	MRWordCounter.run()
