
def merge_sort(unsorted_list):
    if len(unsorted_list)<=1:
        return unsorted_list
    ##middle element
    middle_element=len(unsorted_list)//2
    left_side=unsorted_list[:middle_element]
    right_side=unsorted_list[middle_element:]

    left_side=merge_sort(left_side)
    right_side=merge_sort(right_side)
    return list(merge(left_side,right_side))

def merge(left_half,right_half):
    res=[]
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0]<right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])

        else:
            right_half[0]<left_half[0]
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half)==0:
        res=res+left_half
    else:
        len(right_half)==0
        res=res+right_half

    return res
