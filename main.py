
#Task 1
number_list = [1, 0, -52, 3, 5, -8, 13, 21, 34, -55, 8]
i = 0
for i in range(len(number_list)):
    if number_list[i] <= 5:
        print(number_list[i])

#Task 2(V1)
numbers_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
res = list(set(numbers_1) & set(numbers_2))
print ('TASK 2, V1:', res)

#Task 2(V2)
def Task2():
    numbers_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    res = [i for i in numbers_1 if i in numbers_2]
    print ('TASK 2, V2:', res)
Task2()

#Task 3
def Task3():
    print ('TASK 3')
    list_items = raw_input('Enter values in the list: ').split()
    i = 0
    print ("First value is", list_items[i], "and the last value is:", (list_items[-1]))
Task3()

#Task 4
def Task_4():
    print ('TASK 4')
    list_items = raw_input('Enter numbers string:')
    cortege_items = tuple(list_items)
    set_items = set(list_items)
    print 'list items:', list_items
    print 'cortege items:', cortege_items
    print 'set items', set_items
Task_4()

#Task_5
print ('TASK 5')
a = 'fdgfgbgng'
d = {}
for i in a:
    d.update({i : a.count(i)})
print(d)

#Task_6
print ('TASK 6')
a = 'Automation sometimes helps project and sometimes does not.'
lst = a.split()
count = {}
def maxWord():
    for i in lst:
            max_word = max(lst, key=len)
            print("Max word: " + max_word)
            break
maxWord()
def repWord():
    for i in lst:
        if i not in count:
            count[i] = 0
        else:
            count[i] = 1
            print("Duplicate words: " + i)
repWord()

#Task_7
print ('TASK 7')
string = "Exception breakpoints: suspend the program when Exception or its subclasses are thrown.In PyCharm, you can set breakpoints for Python exceptions."
string.replace(' ', '_')
print(string)

#Task_8
print ('TASK 8')
class Test():
    def A(self):
        string = raw_input('Enter a string: ')
        symbol = raw_input('Enter a symbol: ')
        if symbol in string:
            print({symbol: string.count(symbol)})
        else:
            print('Entered symbol is not in the string')
E = Test()
E.A()

#Task_9
print ('TASK 9')
class Test2():
    def B(self):
        word = raw_input('Enter a word: ')
        if word == word[::-1]:
            print('palindrom')
        else:
            print ('ne palindrom:D')
E2 = Test2()
E2.B()

#Task_10
print ('TASK 10')
my_dict = {'a': 234, 'b': 34, 'c': 375, 'd': 934, 'e': 5271, 'f': 1945}
d = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[0:3]
for key, value in d:
    print(key)


