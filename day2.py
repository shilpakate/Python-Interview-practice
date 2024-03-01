#drop duplicates
# list=[1,2,2,2,3,4]
# lt=[]
# for i in list:
#     if i not in lt:
#         lt.append(i)
# print(lt)
# print(type(lt))

list=[1,2,3,4,4]
a=len(list)
lst=[]
for i in range(0,a-1):
    if(list[i]!=list[i+1]):
        lst.append(list[i])

lst.append(list[-1])
print(lst)

# my_list = [1, 2, 3, 4, 4]
# unique_list = []
# a=len(my_list)
# for i in range(0,a-1):
#     if my_list[i] != my_list[i + 1]:
#         unique_list.append(my_list[i])
#
# # Append the last element since it's not checked in the loop
# unique_list.append(my_list[-1])
#
# print("Unique elements:", unique_list)

# # Sum of elements
# list=[1,2,3,4,5]
# sum=0
# for i in list:
#     sum=sum+i
# print(sum)

# #muplication of list element:
# list=[1,2,3,4,5,6,8]
# product=1
# for i in list:
#     product=product*i;
# print(product)

# #find minimum in list
# num=[91,2,3,4,67]
# min=num[0]
# for i in num:
#     if i < min:
#         min=i
# print("Minimum",min)

#find 2nd highest number from List
num=[1,2,99]
num.sort(reverse=True)
if len(num)>=2:
        Second_highest=num[1]
        print("2nd highest number is",Second_highest)
else :
         print("List not conatin 2nd highest")

