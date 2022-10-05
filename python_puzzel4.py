""" Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings."""


from syslog import LOG_EMERG


ss = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']

def test(str1):
    return str1[len(str1)-2] in str1[len(str1)-1] and str1[len(str1)-2] != str1[len(str1)-1]




for i in range(len(ss)-1):
    
    print(ss[i])


