# The clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make the 'past' function return the time converted to milliseconds.
# More examples in the test cases below.

def past(h,m,s):
    totals= (h*60*60)+(m*60)+s
    ms= 1000 * totals
    return ms
past(1,0,0)
