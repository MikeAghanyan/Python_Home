# ----------------------------------
'''BOOOK - 173'''

# def summ_recurs(a:int, s = 0) -> int:
#     h = 0
#     if a == '':
#         return h
#     elif isinstance(a, int):
#         h += a
#         return summ_recurs(a, h + int(a))
# print(summ_recurs(input('Enter a number ---> ')))

# ----------------------------------
'''BOOOK - 181'''

# def coins(number, coin_count):
#     if coin_count == 0:
#         return number == 0 and coin_count == 0
#     return coins(number - 1, coin_count - 1) or coins(number - 5, coin_count - 1) or coins(number - 10, coin_count - 1) or coins(number - 25, coin_count - 1)
# print(coins(int(input('Enter a number ---> ')), int(input('Enter the coins number ---> '))))

# ----------------------------------
'''BOOOK - 184'''

# def flattering(mylist:list) -> list:
#     if  mylist == []:
#         return []
#     elif isinstance(mylist[0], int):
#         return [mylist[0]] + flattering(mylist[1:])
#     else:
#         return flattering(mylist[0]) + flattering(mylist[1:])
# print(flattering([1, [2, 3], [4, [5, [6, 7]]], [[[8],9], [10]]])) 

# ----------------------------------
'''BOOOK - 185'''

# def count_letters(mylist:list[any], newlist:list[None]=[], count:int=0) -> list[str]:
#     if len(newlist) == len(mylist) // 2:
#         newlist = ''.join(newlist)
#         return list(newlist)
#     else:
#         newlist.append([mylist[count] * mylist[count + 1]])
#         return count_letters(mylist, newlist, count + 2)
# print(count_letters(["A", 12, "B", 4, "A", 6, "B", 1]))

# a = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
# def count(a:list) -> list:
#     mylist = []
#     count_a = 0
#     if count_a == len(a):
#         return mylist
#     for i in a:
#         if mylist[i] != mylist[i] + 1:
#             mylist.append(count)
#             count = 0
#         else:
#             mylist.append(a(i))
#             count += 1
# print(count())
