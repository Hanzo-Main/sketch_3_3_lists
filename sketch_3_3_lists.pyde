# Course: CS 30
# Period: 1
# Date created: 21/01/11
# Date last modified: 21/01/11
# Name: Kira Gray
# Description: practice question 3-3, list of transports with messages

transport = ['car', 'bicycle', 'bus', 'airplane']
txt1 = "I want to get a {}."
txt2 = "I can't ride a {}."
txt3 = "I stopped taking the {} after covid started."
txt4 = "I've been on an {}."

print(txt1).format(transport[0])
print(txt2).format(transport[1])
print(txt3).format(transport[2])
print(txt4).format(transport[3])
