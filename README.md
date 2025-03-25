# ⏱️ `elapsed_by_keyword`

**A small CLI tool to extract and analyze keyword performance from Robot Framework output files.**

This script parses a Robot Framework `output.xml` file and displays the **total elapsed time** and **number of calls** for each keyword used in the test suite sorted by execution time.

It’s a simple way to **identify performance bottlenecks** in your test portfolio.

---

## Example

Let’s say you have the following Robot test case:

    *** Test Cases ***
    My Test
        sleep  1
        sleep  2
        my sleep 5 seconds
        my sleep 5 seconds
    
    *** Keywords ***
    my sleep 5 seconds    
        sleep  5

You execute it with Robot Framework:
```
$ robot tc.robot 
==============================================================================
Tc
==============================================================================
My Test                                                               | PASS |
------------------------------------------------------------------------------
Tc                                                                    | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Output:  /path/to/output.xml
Log:     /path/to/log.html
Report:  /path/to/report.html
```

And then analyze keyword performance:
```
+----------------------------------------+--------------------+------------+
| Keyword Name                           | Total Elapsed Time | Nb of Calls|
+========================================+====================+============+
| Sleep                                  |         0:00:13.00 |     4      |
| My Sleep 5 Seconds                     |         0:00:10.00 |     2      |
+----------------------------------------+--------------------+------------+
```