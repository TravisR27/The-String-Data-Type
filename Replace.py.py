# This task will explain how to replace characters in a string.
word = "The!quick!brown!fox!jumps!over!the!lazy!dog." # this is your sentence that you want to replace.
rep_word = word.replace ("!", " ") # Here is your replacment characters so i want to replace every ! and add a space between words.
print(rep_word) # output will be my replacment word which is what you want it to print.

# this next stage will be showing how to print the sentence all in capital letters.
word2 = "The quick brown fox jumps over the lazy dog." # this is your sentence that you want to replace to make all characters upper case
upper_word2 = word2.upper () # creating this code will make your variable word2 all upper case
print(upper_word2) # this will output word to in upper case characters.

# This next stage will reverse the sentence to read backwards
word3 = "The quick brown fox jumps over the lazy dog." # this is your sentence that you want to replace and put in reverse order
position = word3 [::-1] # set a new variable as position and when doing so because your indexing the characters you will need remember that
#front to back you will start with a 0 because that would be your first digit as a computer would read rather than a human, as they would start with 1 meaning it would miss the first letter.
# once done you will do the same in reverse and start with -1, by using the colon to represent the start of the string and another colon as your stepping value putting -1 will start from the end of the string and reverse it.
print(position) # this will print your variable word in reverse.
