#!/usr/bin/env python

"""Usage: elapsed_by_keyword inpath 

Return the total time elapsed in every keyword on the standard output
Only first level keywords are taken into account
"""

import sys
from robot.api import ExecutionResult, ResultVisitor

class ExecutionKeywordStats(ResultVisitor):

    def __init__(self):
        self.elapsed_by_kw = {}

    def visit_keyword(self, keyword):
        if keyword.name in self.elapsed_by_kw:
            self.elapsed_by_kw[keyword.name] = self.elapsed_by_kw[keyword.name] + keyword.elapsedtime
        else:
            self.elapsed_by_kw[keyword.name] = keyword.elapsedtime

def stats_by_keywords(inpath):
    
    result = ExecutionResult(inpath)
    visitor = ExecutionKeywordStats()    
    result.visit(visitor)
    for kw in sorted(visitor.elapsed_by_kw, key=visitor.elapsed_by_kw.get, reverse=True):
      print kw, visitor.elapsed_by_kw[kw]

if __name__ == '__main__':
    try:
        stats_by_keywords(*sys.argv[1:])
    except TypeError:
        print __doc__