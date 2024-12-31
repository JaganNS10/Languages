import random

#a=random.randint(1,5) #provide the random integer number from 1 To 5 not 5 
#a=random.randrange(1,3) # same as randint
#a=random.random() #It provide the random float number from 0.0<1.0 not 1.0 
#a=random.uniform(1,3) #It provide the random float number using range 
#It select any element from list using choice 
"""list=[1,2,3,"jagan",9,10] 
a=random.choice(list)
print(a)"""

#It shuffle the list using random.shuffle() method
list=[1,2,3,"jagan",8,9,10]
random.shuffle(list)
print(list)