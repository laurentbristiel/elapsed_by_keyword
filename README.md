elapsed_by_keyword
==================

Return the total time elapsed and occurrence of every keyword on the standard output.

This can be useful to work on the performance of a test porfolio.

For example, let's take this test case:

    *** Test Cases ***
    My Test
        sleep  1
        sleep  2
        my sleep 5 seconds
        my sleep 5 seconds
    
    *** Keywords ***
    my sleep 5 seconds    
        sleep  5

We can execute it with Robot Framework and then check the stats by keywords:
    
    $ pybot tc.txt 
    ==============================================================================
    Tc                                                                            
    ==============================================================================
    My Test                                                               | PASS |
    ------------------------------------------------------------------------------
    Tc                                                                    | PASS |
    1 critical test, 1 passed, 0 failed
    1 test total, 1 passed, 0 failed
    ==============================================================================
    Output:  /path/elapsed_by_keyword/output.xml
    Log:     /path/elapsed_by_keyword/log.html
    Report:  /path/elapsed_by_keyword/report.html
    
    $ ./elapsed_by_keyword.py output.xml 
    BuiltIn.Sleep    0:00:13    4
    my sleep 5 seconds    0:00:10    2
