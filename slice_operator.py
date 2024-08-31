def slice_string(object, start, end, step):
    text = ""
    for i in range(start, end, step):
        text += object[i]
    return text


def con1(object, slicing_parameter):
    step = 1
    fist = 0
    last = len(object)
    return slice_string(object, fist, last, step)


def con2(object, slicing_parameter):
    step = slicing_parameter[2]
    first = slicing_parameter[0]
    last = slicing_parameter[1]
    return slice_string(object, first, last, step)
    
print(slice_string("sggggs",0,3,1))
