#6.9 tehtävät 1-10
#All of the exercises below should be added to a single file. In that file, you should also add the test and test_suite scaffolding functions shown above, and then, 
# as you work through the exercises, add the new tests to your test suite. (If you open the online version of the textbook, you can easily copy and paste the tests and the fragments of code into your Python editor.)
#
#After completing each exercise, confirm that all the tests pass.
#
#6.9.1
#The four compass points can be abbreviated by single-letter strings as “N”, “E”, “S”, and “W”. Write a function turn_clockwise that takes one of these
# four compass points as its parameter, and returns the next compass point in the clockwise direction. Here are some tests that should pass:
import sys

def turn_clockwise(direction):
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"
    else:
        return "None"
#Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assume day 0 is “Sunday”. 
# Once again, return None if the arguments to the function are not valid.
def day_name(day):
    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    else:
        return None

#Write the inverse function day_num which is given a day name, and returns its number:
#Once again, if this function is given an invalid argument, it should return None:
def day_num(day):
    if day == "Sunday":
        return 0
    elif day == "Monday":
        return 1
    elif day == "Tuesday":
        return 2
    elif day == "Wednesday":
        return 3
    elif day == "Thursday":
        return 4
    elif day == "Friday":
        return 5
    elif day == "Saturday":
        return 6
    else:
        return None

#Write a function days_in_month which takes the name of a month, and returns the number of days in the month. Ignore leap years:
def days_in_month(month):
    if month == "January":
        return 31
    elif month == "February":
        return 28
    elif month == "March":
        return 31
    elif month == "April":
        return 30
    elif month == "May":
        return 31
    elif month == "June":
        return 30
    elif month == "July":
        return 31
    elif month == "August":
        return 31
    elif month == "September":
        return 30
    elif month == "October":
        return 31
    elif month == "November":
        return 30
    elif month == "December":
        return 31
    else:
        return None

#Write a function to_secs that converts hours, minutes and seconds to a total number of seconds. Here are some tests that should pass:
#Extend to_secs so that it can cope with real values as inputs. It should always return an integer number of seconds (truncated towards zero):
def to_secs(hours, minutes, seconds):
    return int(hours * 3600 + minutes * 60 + seconds)

#Write three functions that are the “inverses” of to_secs
#hours_in
#minutes_in
#seconds_in
#Each of these functions takes a number of seconds, and returns the equivalent amount of time in the given units.
def hours_in(seconds):
    return seconds // 3600

def minutes_in(seconds):
    return seconds % 3600 // 60

def seconds_in(seconds):
    return seconds % 3600 % 60


#Write a function that helps answer questions like ‘“Today is Wednesday. I leave on holiday in 19 days time. What day will that be?”’ 
# So the function must take a day name and a delta argument — the number of days to add — and should return the resulting day name:
def day_add(day, delta):
    if day_num(day) == None:
        return None
    else:
        return day_name((day_num(day) + delta) % 7)


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():

    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)
    #6.9.10 Which of these tests fail? Explain why.
    test(3 % 4 == 0)
    #epäonnistuu, koska 3 ei ole jaollinen 4:llä
    test(3 % 4 == 3)
    #onnistuu, koska 3 on jaollinen 4:llä
    test(3 / 4 == 0)
    #epäonnistuu, koska 3 ei ole jaollinen 4:llä
    test(3 // 4 == 0)
    #onnistuu, koska 3 on jaollinen 4:llä
    test(3+4  *  2 == 14)
    #onnistuu, koska 3+4*2=14
    test(4-2+2 == 0)
    #epäonnistuu, koska 4-2+2=4
    test(len("hello, world!") == 13)
    #onnistuu, koska on yhteensä 13 merkkiä


test_suite()