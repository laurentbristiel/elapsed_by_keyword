#!/usr/bin/env python
"""Usage: elapsed_by_keyword path/to/output.xml 

Reads result of a test run from Robot output file
and outputs "keyword elapsed_time"
sorted by the elapsed time in each keyword.
"""

import datetime
import sys

from robot.api import ExecutionResult, ResultVisitor


class ExecutionKeywordStats(ResultVisitor):
    def __init__(self):
        self.stats_by_kw = {}

    def end_keyword(self, keyword):
        if keyword.name in self.stats_by_kw:
            self.stats_by_kw[keyword.name]['elapsedtime'] += keyword.elapsedtime
            self.stats_by_kw[keyword.name]['count'] += 1
        else:
            self.stats_by_kw[keyword.name] = {'elapsedtime': keyword.elapsedtime, 'count': 1}


def stats_by_keywords(path):

    result = ExecutionResult(path)
    visitor = ExecutionKeywordStats()
    result.visit(visitor)
    for kw in sorted(visitor.stats_by_kw, key=lambda kw: visitor.stats_by_kw[kw]['elapsedtime'], reverse=True):
        print('{0}\t{1}\t{2}'.format(kw,
                                     str(datetime.timedelta(milliseconds=visitor.stats_by_kw[kw]['elapsedtime']))[:-7],
                                     visitor.stats_by_kw[kw]['count']))


if __name__ == '__main__':
    try:
        stats_by_keywords(*sys.argv[1:])
    except TypeError:
        print(__doc__)
