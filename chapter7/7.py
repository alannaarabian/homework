import sys
##
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    print("tests for turn clockwise")
    test(count_odd(numlist) == 5)
 
    
numlist = [0,1,2,3,4,5,6,7,8,9,10]

def count_odd(oddlist):
    count = 0
    for i in oddlist:
        if i % 2 != 0:
            count += 1
    return count
    
test_suite()


        
    