
# Q-22 : Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. Ifthe string length islessthan 2,return instead of the empty
# string.

def string1(str):
    if len(str) < 2:
        return ""
    else:
        return str[0:2] + str[-2:]

print(string1("Hello World"))
print(string1("Hi"))
print(string1("H"))