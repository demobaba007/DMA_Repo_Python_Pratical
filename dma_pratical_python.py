class Set:
    def input():
        array = []
        num = int(input("Enter the numnber of element : "))
        for i in range(num):
            element = int(input("Enter the element : "))
            array.append(element)
        return array
    def unique(elements):
        array = []
        for i in elements:
            if i in array:
                pass
            else:
                array.append(i)
        print("{ Φ",end="")
        for j in array:
            print(" ,",j, end="")
        print("}")
        return array
    def output(lenght_of_element):
        print("Cardinality of a set or |set|: ", len(lenght_of_element))
    def ismember(array, num):
        if num in array:
            return 1
        else:
            return 0

obj = Set
input_func = obj.input()
unique_func = obj.unique(input_func)
output_func = obj.output(unique_func)

print("Finding the element is present in set or not : ")
number = int(input("Enter the number : "))
if obj.ismember(unique_func, number) == 1:
    print(True)
else:
    print(False)