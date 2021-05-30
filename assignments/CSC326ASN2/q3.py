def my_map(function, iterable):
    if iterable == None:
        return []
    if function == None:
        return [i for i in iterable]
    return [function(i) for i in iterable]

def my_filter(function, iterable):
    if iterable == None:
        return None
    if function == None:
        return iterable
    if type(iterable) == str:
        return ''.join([i for i in iterable if function(i)])
    if type(iterable) == tuple:
        return tuple([i for i in iterable if function(i)])
    # a list iterable
    return [i for i in iterable if function(i)]

def my_reduce(function, iterable):
    if function == None:
        return iterable
    if iterable == None:
        return None

    i = iter(iterable)
    result_accu = i.next()
    for item in i:
        result_accu = function(result_accu, item)
    return result_accu


print my_map(lambda x: x*2, [1,2,3])
print my_map(None, [1,2,3])
print my_map(lambda x: x*3, [])
print my_map(lambda x: x*2, '123')
print my_map(lambda x: x*2, None)

print my_filter(lambda x: x & 1 == 0, [1,2,3,4])
print my_filter(None, '123')
print my_filter(lambda x: x, None)
print my_filter(lambda x: x, (1,2,3))
print my_filter(lambda x: x == '2', "123")


print my_reduce(lambda x,y : x+y, [1,2,3])
print my_reduce(lambda x,y : x*y, [1,2,3])
print my_reduce(lambda x,y : x+y, None)
print my_reduce(None, [1,2,3])
print my_reduce(None, [1,2,3])


