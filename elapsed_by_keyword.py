#!/usr/bin/env python3
"""Usage: elapsed_by_keyword path/to/output.xml 

Reads result of a test run from Robot output file and outputs "keyword elapsed_time"
sorted by the elapsed time in each keyword.
"""

import datetime
import sys
import os

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


def print_stats_table(stats_by_kw):
    # Define column headers
    headers = ["Keyword Name", "Total Elapsed Time", "Nb of Calls"]
    col_widths = [40, 20, 12]

    # Print top border
    print("+" + "+".join(["-" * w for w in col_widths]) + "+")

    # Print header row
    print("|{:<40}|{:^20}|{:^12}|".format(*headers))

    # Print separator
    print("+" + "+".join(["=" * w for w in col_widths]) + "+")

    # Print data rows
    for kw in sorted(stats_by_kw, key=lambda kw: stats_by_kw[kw]['elapsedtime'], reverse=True):
        duration = str(datetime.timedelta(milliseconds=stats_by_kw[kw]['elapsedtime']))[:-4]
        count = stats_by_kw[kw]['count']
        print("|{:<40}|{:>20}|{:^12}|".format(kw, duration, count))

    # Print bottom border
    print("+" + "+".join(["-" * w for w in col_widths]) + "+")

def stats_by_keywords(path):

    result = ExecutionResult(path)
    visitor = ExecutionKeywordStats()
    result.visit(visitor)
    print_stats_table(visitor.stats_by_kw)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python elapsed_by_keyword.py path/to/output.xml")
        sys.exit(1)

    xml_path = sys.argv[1]

    if not os.path.exists(xml_path):
        print(f"Error: File not found – {xml_path}")
        sys.exit(1)

    try:
        stats_by_keywords(xml_path)
    except Exception as e:
        print(f"An error occurred while processing: {e}")
        sys.exit(1)