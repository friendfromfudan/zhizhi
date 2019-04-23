def next_id(arr):
    if not arr:
        return 0
    sort_arr=set(sorted(arr))
    array=set(range(0,max(array)+1))
    gap=array