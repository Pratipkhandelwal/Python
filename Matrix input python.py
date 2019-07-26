import numpy

n,m = map(int,raw_input().split())
my_array = numpy.array([raw_input().strip().split() for _ in range(n)],int)
print (numpy.transpose(my_array))
print ((my_array).flatten())



#SPACING ISSUE

numpy.set_printoptions(sign=' ')
print(numpy.eye(*map(int, input().split())))

