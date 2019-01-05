mydict = {'carl':40, 'alan':2, 'bob':1, 'alan':3}

l = mydict.keys()

print ('Sort by keys:')
for key in sorted(mydict.keys()):
    print ("%s: %s" % (key, mydict[key]))
print(sorted(l))
