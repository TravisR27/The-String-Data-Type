# This task will show how to manipulate a string and strip a word.
hero = "$$$Superman$$$" # this is the word that needs to be stripped
strip_hero = hero.strip ("$") # this shows what characters need to be stripped from the word without specifying it wont strip, this will remove all $ from the front and end of the word.
print(strip_hero) # this output will print the strip word and remove all $