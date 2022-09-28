
# changing index and printing separately
l1=["eat","sleep","pray"]
l2=["twice"]
for count, ele in enumerate(l1,100):
    print(count,ele)

""" Output 
100 eat
101 sleep
102 pray"""

# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]
  
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)

""" Output
(0, 'eat')
(1, 'sleep')
(2, 'pray')
"""
# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)

""" Output
0
eat
1
sleep
2
repeat
"""