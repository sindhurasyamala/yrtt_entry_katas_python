# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
# Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
# More examples in the test cases below.

# Good luck!

def repeats(arr):
    dict = {}
    lis = []
    for ele in arr:

        try:
            dict[ele] += 1
        except:
            dict[ele] = 1

    for item in dict:
        if (dict[item] <= 1):
            lis.append(item)
    # print("repeated numbers= ", lis)
    s = 0
    for x in lis:
        s = s + x
    return s

repeats([4,5,7,4,5,8])