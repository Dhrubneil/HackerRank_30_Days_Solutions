class Difference:
    
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    maximumDifference = 0#INSTANCE VARIABLE

    def computeDifference(self):
        print("This method will print the max abs diff. of the list ", self.__elements)

        for ele in self.__elements:
            for i in range(0,len(self.__elements)):
                diff = abs(ele - self.__elements[i])
                self.maximumDifference = max(diff, self.maximumDifference)
                #print(self.maximumDifference)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
