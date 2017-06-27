# -*- set coding:utf-8 -*-
#!/user/bin/env python


from mrjob.job import MRJob
from mrjob.step import MRStep
import re


class MRCounter(MRJob):
    """docstring for MRCounter"""

    def get_time_uid(self,_,line):
        value = re.match('(\d{8}\s\d{4}).+\[(.+@.+\w)\s-\s',line)
        if value is not None:
            Time,Uid = value.groups()
            Time_Uid = "%s_%s" % (Time,Uid)
            yield Time_Uid,1

    def combiner_time_uid(self,Time_Uid,value):
        #合并相同的time value
        yield Time_Uid,1

    def mapper_time_uid(self,Time_Uid,value):
        Time,Uid = Time_Uid.split("_")
        yield Time.replace(' ','_'),1

    def reducer_users_count(self,Time,occurrences):
        yield Time.replace(' ','_'),sum(occurrences)

    def steps(self):
        return [
        MRStep(mapper=self.get_time_uid,
            combiner=self.combiner_time_uid),
        MRStep(mapper=self.mapper_time_uid,
            reducer=self.reducer_users_count)
        ]

if __name__ == '__main__':
    MRCounter.run()