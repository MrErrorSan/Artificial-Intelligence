# -*- coding: utf-8 -*-
"""Lab#2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sw_MyPD_DB8HbGWyKmpnFFj86hFzZfSJ
"""



p0 = ['Mercury', 'Venus','Earth','Mars']
p1 = ['Mercury', 'Venus','Earth','Mars']
no=[1,2,3,4,5,6,7,8,9,0]
planets = [p0,p1]
#planets.append(p0)
#for i in planets:
#  print(" ")
#  for i1 in range(4):
#    print(i[-1-i1])

#print(len(planets))

#print(planets)


#print(p0[0:3])


#p0[:2]=['a','b']
#print(p0)

# print(p0.count('Mars'))
# print(p0.index('Mars'))

#p0.sort(reverse = True)
#print(p0)

#no.pop()
#del no[9]
#print(min(no))
#print(max(no))
#print(sum(no))

#'Pluto' in p0
#'Mars' in p0

#squares = [n**9 for n in range(3)]
#print(squares)

#print(p0[2].upper()+'!')

def count_negatives(nums):
  # False + True + True + False + False equals to 2.
  # return len([num for num in nums if num &lt; 0])
  return sum([num < 0 for num in nums])
#count_negatives([5, -1, -2, -0, -3])

# a = 1
# b = 0
# print(a,b)
# a, b = b, a
# print(a,b)

x = input('Enter String : ')
sp=x.split()
print('3rd word is : ' + sp[2])

def CountFrequency(my_list,n):
  freq = {}
  for z in range(0,n):
    for item in my_list[z]:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
  return freq
def get_key(my_dict,val):
    for key, value in my_dict.items():
         if val == value:
             return key
if __name__ == "__main__":
    from random import randint
    n = 5
    grid = [[randint(1, 5) for _ in range(n)] for i in range(n)]
    disc = {}
    print(grid)
    disc=CountFrequency(grid,n)
    print(disc)
    l=list(disc.values())
    l.sort(reverse = True)
    print("1st Highest",get_key(disc,l[0]))
    disc.pop(get_key(disc,l[0]))
    print("2nd Highest",get_key(disc,l[1]))
    disc.pop(get_key(disc,l[1]))
    print("3rd Highest",get_key(disc,l[2]))

d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
print("All the users whose phone number ends in an 8")
for a in range (0,4):
  if d[a]['phone'][-1]=='8':
    print(d[a]['name'])
print("All the users that don???t have an email address listed")
for a in range (0,4):
  if d[a]['email']=="":
    print(d[a]['name'])