import sys;
l=[];
n=int(raw_input("Enter the size of the list\n"));
i=0;
for i in range(n):
	l.append(raw_input("Enter the value\n"));
print l;
	

cmp(list1, list2)

Compares elements of both lists.
2	

len(list)

Gives the total length of the list.
3	

max(list)

Returns item from the list with max value.
4	

min(list)

Returns item from the list with min value.
5	

list(seq)

Converts a tuple into list.

6	

list.append(obj)

Appends object obj to list
7	

list.count(obj)

Returns count of how many times obj occurs in list
8	

list.extend(seq)

Appends the contents of seq to list
9	

list.index(obj)

Returns the lowest index in list that obj appears
10	

list.insert(index, obj)

Inserts object obj into list at offset index
11	

list.pop(obj=list[-1])

Removes and returns last object or obj from list
12	

list.remove(obj)

Removes object obj from list
13	

list.reverse()

Reverses objects of list in place
14	

list.sort([func])

Sorts objects of list, use compare func if given

