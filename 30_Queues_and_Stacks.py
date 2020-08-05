import sys

class Solution:
    myStack = []
    myQueue = []
    def pushCharacter(self, myChar):
        self.myStack.append(myChar)
    
    def enqueueCharacter(self, myChar):
        self.myQueue.append(myChar)

    def popCharacter(self):
        return self.myStack.pop()

    def dequeueCharacter(self):
        return self.myQueue.pop((0))

    # Write your code here

# read the string s
s=input("Enter a string to check whether it's a palindrome or not: ")
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

print(obj.myStack, obj.myQueue)    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    

print(obj.myStack, obj.myQueue)