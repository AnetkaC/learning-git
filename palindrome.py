def reverse(s): 
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s) 
  
# Sprawdzenie czy oba wyrazy są sobie równe 
    if (s == rev): 
        return True
    return False
  
s = input("Proszę wprowadź wyraz do sprawczenia czy jest palindromem: ")
ans = isPalindrome(s)
  
if ans == 1: 
    print("TAK, podany wyraz to palindrom")
else: 
    print("NIE, podany wyraz to nie palindrom") 

