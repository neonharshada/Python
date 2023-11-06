# 1) accept a string and display whether it is palindrom or not.
str=input("Enter a string:").lower()
if str == str[::-1]:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrom")

# 2) accept a string and display it. now accept slicing positions from and to , slice the string and display it.
str = input("Enter a string:")
print("Ogi String:",str)
start=int(input("Enter a from position:"))
end=int(input("Enter a to position:"))
slice_str=str[start:end]
print("sliced str",slice_str)

# 3) accept a string and display how many vowel characters are there inside it.
str = input("Enter a string:").lower()
vowel_count = 0
vowel = ['a', 'e', 'o', 'i', 'u']
for i in str:
    if i in vowel:
        vowel_count += 1
print("Number of vowels:", vowel_count)

# 4) accept a string and display the characters which are repeated in the string
mystr = input("Enter a string:").lower()
reapeted_char = []
for i in mystr:
    if mystr.count(i) > 1 and i not in reapeted_char:
        reapeted_char.append(i)
print("reapeted character in string:", reapeted_char)


# 5) accept a string and find out how many words are there in it.
str1=input("Enter a string:")
words=str1.split()  #spiting the string
words_count = len(words)
print(words_count)

# 6) accept a sentence and reverse it.
# 	e.g.  hello world
# 		world hello
sen = input("Enter a sentence:")
words=sen.split()
reverse_word=words[::-1]
print("reverse sentence:",reverse_word)


# 7) A pangram is a sentence that contains all the alphabets.
# example: The quick brown fox jumps over the lazy dog. Your task here is to
# write a function to check a sentence to see if it is a pangram or not.
sentence= input("Enter a sentence:").lower()
myset=['abcdefghijklmnopqrstuvwxyz']
for i in sentence:
    if i.isalpha():
        if i in myset:
            print(f"{sentence} is pangram")
else:
        print(f"{sentence} is not pangram") #it is wrong













