import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
# ///////////////////Create a list of numbers
list = []
for i in range(1, n):
    list.append(sys.argv[i])
# ///////////////////Check even numbers
print('The even numbers of the input are the following:')
counter = 0
sum = 0
for i in list:
    if (float(i) % 2) == 0:
        print(str(i), end = ' ')
        counter = counter + 1
        sum = sum + int(i)
# Average of numbers
average = float(sum) / float(counter)
res = "{:.2f}".format(average)
print('\nAverage of the numbers is '+str(res)+'.')

