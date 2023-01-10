# exercise for fun
# def somthing(*sum):
#     my_sum = 0
#     for num in sum:
#         my_sum+=num
#     avg=my_sum/len(sum)
#     return avg
# somthing_else=somthing(10,20,30,40,50,60)
# print(somthing_else)

# homework
# exercise1
# option1
# def parameter (parameter2:str):
#     parameter3=parameter2.split("-")
#     parameter3.sort()
#     return parameter3
# print(parameter("green-red-yellow-black-white"))

#option2

# def parameter (parameter2:str):
#     parameter3=parameter2.split("-")
#     parameter3.sort()
#     return parameter3
# n=input("insert str")
# print(parameter(n))

#exercise3

# def string_test(s:str):
#     upper_case=0
#     lower_case=0
#     for i in s:
#         if i.islower():
#             lower_case+=1
#         elif i.isupper():
#             upper_case+=1
#     return upper_case,lower_case
#
# print(string_test("HELLo"))

# exercise4
# def is_pangram(sentence:str):
#     alphabet = ("abcdefghijklmnopqrstuvwxyz")
#     for i in alphabet:
#         if i not in sentence:
#             return False
#     return True
#
# string=input("insert a string")
# if is_pangram(string)==True:
#     print("your sentence is pangram")
# else:
#     print("your sentence is not pangram")

# exercise5
# def is_palindrome (sentence:str):
#     l=sentence[::-1]
#     if sentence==l:
#         return True
#     return False
#
# sen=input("insert a sentence")
# if is_palindrome(sen)==True:
#     print("your sentence is palindrome  ")
# else:
#     print("your sentence is not palindrome  ")







