'''positive list of numbers'''
List1=[2,4,-6,-8,9,7]
List2=[i for i in List1 if(i>0)]
print(f"Positive numbers are: {List2}")

'''Square of N numbers'''
list1=[1,2,3,4,5,6]
list2=[i**2 for i in list1]
print(list2)

'''vowels in a word'''
word=(input("Enter the word: "))
list_vowel=[i for i in word if i in 'aeiouAEIOU']
print(f"Vowels are {list_vowel}")

'''ordinal value'''
w=input("Enter any character:")
OrdinalVal=[ord(i) for i in w]
print(OrdinalVal)
