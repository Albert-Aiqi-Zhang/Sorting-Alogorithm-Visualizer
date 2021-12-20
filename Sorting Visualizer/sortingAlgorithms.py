def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True
    return lst

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(1, len(lst)):
        current = lst[i]
        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending
            if not ascending_sort and not descending_sort:
                break
            lst[i] = lst[i - 1]
            i -= 1
            lst[i] = current
            draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True
    return lst

def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst
    currentIdx = 0
    while currentIdx < len(lst) - 1:
        if ascending:
            smallestIdx = currentIdx
            for i in range(currentIdx + 1, len(lst)):
                if lst[i] < lst[smallestIdx]:
                    smallestIdx = i
                draw_list(draw_info, {currentIdx: draw_info.GREEN, i: draw_info.YELLOW, smallestIdx: draw_info.RED}, True)
                yield True
            lst[smallestIdx], lst[currentIdx] = lst[currentIdx], lst[smallestIdx]
            draw_list(draw_info, {currentIdx: draw_info.GREEN, smallestIdx: draw_info.RED}, True)
            yield True
        else: # descending
            largestIdx = currentIdx
            for i in range(currentIdx + 1, len(lst)):
                if lst[i] < lst[largestIdx]:
                    largestIdx = i
                draw_list(draw_info, {currentIdx: draw_info.GREEN, i: draw_info.YELLOW, largestIdx: draw_info.RED}, True)
                yield True
            lst[largestIdx], lst[currentIdx] = lst[currentIdx], lst[largestIdx]
            draw_list(draw_info, {currentIdx: draw_info.GREEN, largestIdx: draw_info.RED}, True)
            yield True
        currentIdx += 1
    return lst
            
def quick_sort(draw_info, ascending=True): 
    # use an iterative version to adjust the settings in the main function
    lst = draw_info.lst
    l, h = 0, len(lst) - 1

    stack = [0] * len(lst)
    # push initial values of l and h to stack
    top = 0
    stack[top] = l
    top += 1
    stack[top] = h
    # Keep popping from stack whenever it is not empty
    while top >= 0:
        # Pop h and l
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        # Set pivot element at its correct position in
        # sorted array
        i = l - 1
        x = lst[h]
        for j in range(l, h):
            if ascending:
                if lst[j] <= x:
                    # increment index of smaller element
                    i = i + 1
                    lst[i],lst[j] = lst[j],lst[i]
            else: # descending:
                if lst[j] >= x:
                    # increment index of larger element
                    i = i + 1
                    lst[i], lst[j] = lst[j], lst[i]
            draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.YELLOW, l: draw_info.PINK, h: draw_info.RED}, True)
            yield True
        lst[i + 1], lst[h] = lst[h], lst[i + 1]
        p = i + 1
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
    return lst

def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for currIdx in reversed(range(len(lst) // 2)):
        endIdx = len(lst) - 1
        leftChildIdx = currIdx * 2 + 1
        while leftChildIdx <= endIdx:
            rightChildIdx = currIdx * 2 + 2 if currIdx * 2 + 2 <= endIdx else -1
            if ascending:
                if rightChildIdx != -1 and lst[rightChildIdx] > lst[leftChildIdx]:
                    idxToSwap = rightChildIdx
                else:
                    idxToSwap = leftChildIdx
                if lst[currIdx] < lst[idxToSwap]:
                    lst[currIdx], lst[idxToSwap] = lst[idxToSwap], lst[currIdx]
                    currIdx = idxToSwap
                    leftChildIdx = currIdx * 2 + 1
                else:
                    break
            else: # descending
                if rightChildIdx != -1 and lst[rightChildIdx] < lst[leftChildIdx]:
                    idxToSwap = rightChildIdx
                else:
                    idxToSwap = leftChildIdx
                if lst[currIdx] > lst[idxToSwap]:
                    lst[currIdx], lst[idxToSwap] = lst[idxToSwap], lst[currIdx]
                    currIdx = idxToSwap
                    leftChildIdx = currIdx * 2 + 1
                else:
                    break
            draw_list(draw_info, {currIdx: draw_info.GREEN, endIdx: draw_info.YELLOW, leftChildIdx: draw_info.PINK, rightChildIdx: draw_info.RED}, True)
            yield True
    for i in reversed(range(1, len(lst))):
        lst[0], lst[i] = lst[i], lst[0]
        currIdx = 0
        endIdx = i - 1
        leftChildIdx = currIdx * 2 + 1
        while leftChildIdx <= endIdx:
            rightChildIdx = currIdx * 2 + 2 if currIdx * 2 + 2 <= endIdx else -1
            if ascending:
                if rightChildIdx != -1 and lst[rightChildIdx] > lst[leftChildIdx]:
                    idxToSwap = rightChildIdx
                else:
                    idxToSwap = leftChildIdx
                if lst[currIdx] < lst[idxToSwap]:
                    lst[currIdx], lst[idxToSwap] = lst[idxToSwap], lst[currIdx]
                    currIdx = idxToSwap
                    leftChildIdx = currIdx * 2 + 1
                else:
                    break
            else: # descending
                if rightChildIdx != -1 and lst[rightChildIdx] < lst[leftChildIdx]:
                    idxToSwap = rightChildIdx
                else:
                    idxToSwap = leftChildIdx
                if lst[currIdx] > lst[idxToSwap]:
                    lst[currIdx], lst[idxToSwap] = lst[idxToSwap], lst[currIdx]
                    currIdx = idxToSwap
                    leftChildIdx = currIdx * 2 + 1
                else:
                    break
            draw_list(draw_info, {currIdx: draw_info.GREEN, endIdx: draw_info.YELLOW, leftChildIdx: draw_info.PINK, rightChildIdx: draw_info.RED}, True)
            yield True
    return lst

def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst
    low = 0
    high = len(lst) - 1
    # sort list `lst` using lst temporlstry list `temp`
    temp = lst[:]
 
    # divide the list into blocks of size `m`
    # m = [1, 2, 4, 8, 16…]
 
    m = 1
    while m <= high - low:
        # for m = 1, i = [0, 2, 4, 6, 8…]
        # for m = 2, i = [0, 4, 8, 12…]
        # for m = 4, i = [0, 8, 16…]
        # …
        for i in range(low, high, 2*m):
            frm = i
            mid = i + m - 1
            to = min(i + 2 * m - 1, high)
            k = frm
            i = frm
            j = mid + 1
        
            # loop till no elements are left in the left and right runs
            while i <= mid and j <= to:
                if ascending:
                    if lst[i] <= lst[j]:
                        temp[k] = lst[i]
                        i = i + 1
                    else:
                        temp[k] = lst[j]
                        j = j + 1
                else: # descending
                    if lst[i] >= lst[j]:
                        temp[k] = lst[i]
                        i = i + 1
                    else:
                        temp[k] = lst[j]
                        j = j + 1
                k = k + 1
                draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.YELLOW, k: draw_info.RED, m: draw_info.PINK}, True)
                yield True
            # copy remaining elements
            while i < len(lst) and i <= mid:
                temp[k] = lst[i]
                k = k + 1
                i = i + 1
                draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.YELLOW, k: draw_info.RED, m: draw_info.PINK}, True)
                yield True
            # copy back to the original list to reflect sorted order
            for i in range(frm, to + 1):
                lst[i] = temp[i]
                draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.YELLOW, k: draw_info.RED, m: draw_info.PINK}, True)
                yield True
        m = 2 * m
    return lst