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
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("   ") == None)
    
    print("\nday to name")
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    
    print("\nday name to number")
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    
    print("\nday_add")
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    
    print("\ndays_in_month")
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    print("/nto_secs")
    test(to_secs(2, 30, 10)== 9010)
    test(to_secs(0,2,0)==720)
    test(to_secs(0,2,0)==120)
    test(to_secs(0,0,42)==42)
    test(to_secs(0, -10, 10)== -590)

    test (is_even(2)== True )
    test (is_even(3)== False)
    
    test (is_odd(2)== False)
    test (is_odd(3)== True)
    
    
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))


def is_factor(f,n):
    return n % f == 0

def is_multiple (m,n):
    return is_factor (n,m)
    

    
    
def is_even(n):
    return n % 2== 0

def is_odd(n):
    if is_even(n):
        return False
    else:
        return True
    
    






    
 
    
    
    
def to_secs(hours, minutes, seconds):
    """converts hours, minutes and seconds to a total number of seconds"""
    sec_hour= hours *60 *60
    sec_minutes = minutes * 60

def days_in_month(name):
    """takes a month name and returns the number of days in that month"""
    if name == "January" or name == "March" or name == "May" or name == "July" or name == "August" or name == "October" or name == "December":
        return 31
    elif name == "February":
        return 28
    elif name == "April"  or name == "June"  or name == "November":
        return 30
    
def turn_clockwise(direction):
    """takes a compass point and return the next clockwise point"""
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"
   

def day_name(num):
    """takes a day number 0-6 and return the name"""
    if num == 0:
        return "Sunday"
    if num == 1:
        return "Monday"
    if num == 2:
        return "Tuesday"
    if num == 3:
        return "Wednesday"
    if num == 4:
        return "Thursday"
    if num == 5:
        return "Friday"
    if num == 6:
        return "Saturday"
    else:
        return None

def day_num(day_name):
    """takes a day name and returns a number 0-6"""
    if day_name == "Sunday":
        return 0
    elif day_name ==  "Monday":
        return 1
    elif day_name == "Tuesday":
        return 2
    elif day_name == "Wednesday":
        return 3
    elif day_name == "Thursday":
        return 4
    elif day_name == "Friday":
        return 5
    elif day_name == 6:
        return 6
   

def day_add(name,delta):
    """takes in a day name and a number of days (delta). Adds the delta - returns name of the day."""
    start_day_num = day_num(name)
    end_day_num = start_day_num + delta
    end_day_name = day_name(end_day_num % 7)
    return end_day_name

    
def far_to_cel(Tempfar):
    """
    Input: Tempfar [int]
    Ouput: TempCel [int]
    """
    Tempcel= (Tempfar - 32)/1.8
    Tempcel= round(Tempcel)
    
    return Tempcel
    
def Test_far_to_cel():
    test(far_to_cel(212)== 100)
    test(far_to_cel(32)== 0)
    test(far_to_cel(-40)==-40)
    test(far_to_cel(100)==38)
    
Test_far_to_cel()
  
##test_suite()
### Here is the call to run the tests

