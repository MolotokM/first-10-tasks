
#Task 1
number_list = [1, 0, -52, 3, 5, -8, 13, 21, 34, -55, 8]
i = 0
while i < len(number_list):
    if number_list[i] > 5:
        del number_list[i]
    else:
        i += 1
print ('Task 1 result', number_list)


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
    list_items = raw_input('Enter numbers string:').replace(' ', ',')
    cortege_items = tuple(list_items.replace(',', ''))
    set_items = set(list_items.replace(',', ''))
    print 'list items:', list_items
    print 'cortege items:', cortege_items
    print 'set items', set_items
Task_4()

#Task_5
a = 'fdgfgbgng'
d = {}
print ('TASK 5')
for i in a:
    d.update({i : a.count(i)})
print(d)

#Task_6
a = 'Automation sometimes helps project and sometimes does not.'
lst = a.split()
count = {}
print ('TASK 6')
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

