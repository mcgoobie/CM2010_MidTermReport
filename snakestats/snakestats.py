import math

def mean(vals):
    sum = 0.0
    for i in range(len(vals)):
        sum += float(vals[i])
        
    return sum / len(vals)


def getMax(vals):
    maxSeen = 0
    for i in range(len(vals)):
        if float(vals[i]) > maxSeen:
            maxSeen = float(vals[i])
    return maxSeen


def getMin(vals):
    minNum = 0
    num_list = []
    for val in vals:
        if isinstance(val, str):
            val = int(val)
            num_list.append(val)
        else:
            num_list.append(val)
            
    num_list.sort()
    minNum = num_list[0]
    
    return minNum


def getMode(vals):
    freq = 0
    length = len(vals)
    comp_list = [0] * length
    
    for val in vals:
        count = comp_list[val] + 1
        comp_list[val] = count
        
    if all(comp_list):
        return True
    else:
        max_val = max(comp_list)
        index = comp_list.index(max_val)
        return False, index


# def getFreq(vals):
#     freq = 0
#     length = len(vals)
#     comp_list = [0] * length
    
#     for val in vals:
#         val = math.floor(val)
#         count = comp_list[val] + 1
#         comp_list[val] = count
        
#     if all(comp_list):
#         return True
#     else:
#         max_val = max(comp_list)
#         index = comp_list.index(max_val)
#         return index

    
def getMedian(vals):
    mid = 0
    mid_left = 0
    mid_right = 0
    
    vals.sort()
    if (len(vals) % 2 == 0):
        mid_right = int(len(vals) / 2)
        mid_left = int(mid_right - 1)
        median = (vals[mid_left] + vals[mid_right]) /2
        
        return median
    else:
        mid = len(vals) / 2
        mid = math.floor(mid)
        median = vals[mid]
        return median

