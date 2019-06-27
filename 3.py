s=input()
d=['a','e','i','o','u','A','E','I','O','U']
k=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
if s in d:
  print("Vowel")
elif s in k:
  print("Consonant")
else:
  print("invalid")
