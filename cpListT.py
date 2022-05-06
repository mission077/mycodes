# #*******************************************************************************
# #
# # Programmer: MISSION RAJ KADARIYA
# #
# # Assignment: cpListT.py
# #
# # Description: Lab assignment about the list function.
# #           
# #
# #*******************************************************************************

# # define a list with three elements
# myList = ["abc", 123, "xyz"]

# #use the len() function to determine the number of elements in the list
# # display the value to the screen
# myListLength = len(myList)
# print("\nThe length of myList is", myListLength)

# #display te values of the list to the screen
# print("\nmyList contains the following values:")
# index = 0
# while(index < myListLength):
#     print("index: ", index, "value: ", myList[index])
#     index = index + 1



# # define a list with three elements
# myList = ["abc", 123, "xyz"]
# #use the len() function to determine the number of elements in the list
# # displaty the value to the screen
# myListLength = len(myList)
# print("\nThe length of  myList is", myListLength) 

# #modify the last elemnt of the list
# myList[2] = 987

# #display the values of the list to the screen
# print("\nmyList contains the following values:")
# index = 0
# while (index < myListLength):
#     print("index: ", index, "value: ", myList[index])
#     index = index + 1

# # prompt the user for two more elemnts fo the list
# value1 = float(input("\nENter a decimal value: "))
# value2 = input("Enter your name: ")

# # add the values to the list
# myList.append(value1)
# myList.append(value2)

# # display the values of the list to the screen
# print("\nmyList contains the following values:")
# index = 0
# myListLength = len(myList)
# while (index < myListLength):
#     print("index: ", index, "value: ", myList[index])
#     index = index + 1



# # sort the list and display the list to the screen
# myList.sort( )
# print("\nmyList, now in sorted order:")
# index = 0
# while (index < myListLength):
#     print("index: ", index, "value: ", myList[index])
#     index = index + 1



# # determine the index fo 123
# index = myList.index(123)
# print("\n123 is located at position", index)
# # determine the index of "Hello"
# index = myList.index("Hello")
# print("\nHello is located at position", index)

# # remove the occurence of 123 and display the list
# myList.remove(123)


# print("\nmyList after removing 123:")
# index = 0
# myListLength = len(myList)
# while (index < myListLength):
#     print("index: ", index, "value: ", myList[index])
#     index = index + 1

# del myList[3]
# #create a numerical list
# numList = [12,23,34,45,56]

# myListLength = len(numList)
# print("\nThe length of myList is", myListLength)

# print("\nmyList contains the following values: ")
# index = 0
# while (index < myListLength):
#     print("index: ", index, "value: ", numList[index])
#     index = index + 1
    
# print("The total of the list is: ", sum(numList))

def triangle(a,b,c):
    if (a + b > c) and (b + c > a) and (c + a > b):
        print("valid")
    else:
        print("invalid")
triangle(10,2,1)