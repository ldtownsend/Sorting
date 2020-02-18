# TO-DO: Complete the selection_sort() function below
# Fixing git...
def selection_sort( arr ):
    # loop through n-1 elements
    
    if len(arr) == 0:
        pass
    else:
        for i in range(0, len(arr) - 1):
            cur_index = i
            smallest_index = cur_index
            # TO-DO: find next smallest element
            # (hint, can do in 3 loc) 
            for x in range(i+1, len(arr)):
                if arr[smallest_index] > arr[x]:
                    smallest_index = x
            # Swap using multiple variables/indices separated by a comma
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    if len(arr) == 0:
        pass
    else:
        for i in range(len(arr)):
            for x in range(0, len(arr)-i-1):
                if arr[x] > arr[x+1]:
                    arr[x], arr[x+1] = arr[x+1], arr[x]

    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr