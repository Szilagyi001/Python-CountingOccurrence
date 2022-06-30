occurrence=0
desiredValue=int(input("which number (1-9)do you wish to count?"))

numList=(2, 4, 1, 2, 3, 4, 1, 2, 4, 3, 6, 7, 6, 7, 8, 9, 9, 9, 8, 4, 2, 1)

k = 8

for counter in range(len(numList)):
    if numList[counter]==desiredValue:
        occurrence=occurrence+1


print("the number",desiredValue,"appears",occurrence, "times in the list.")
