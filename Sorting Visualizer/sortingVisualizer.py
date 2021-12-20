### Hopefully I can add some interactive objects in the future.

import pygame
import sys
import random
import math
pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    BLUE = 0, 0, 255
    RED = 255, 0, 0
    GREY = 128, 128, 128
    YELLOW = 255, 250, 100
    PINK = 255, 192, 203
    BACKGROUND_COLOR = WHITE

    FONT = pygame.font.SysFont("Times", 25)
    LARGE_FONT = pygame.font.SysFont("arial", 35)
    SIDE_PAD = 100
    TOP_PAD = 150

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    if ascending:
        title = draw_info.LARGE_FONT.render(algo_name + str(" - Ascending"), 1, draw_info.RED)
    else:
        title = draw_info.LARGE_FONT.render(algo_name + str(" - Descending"), 1, draw_info.RED)
    # "{Sorting algorithm} - {'Ascending' if ascending else 'Descending'}"
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2 , 5))

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 , 45))

    controls = draw_info.FONT.render("LEFT - Increase Numbers | RIGHT - Decrease Numbers", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 , 70))

    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | S - Selection Sort", 1, draw_info.BLUE)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2 , 95))

    sorting = draw_info.FONT.render("Q - Quick Sort | H - Heap Sort | M - Merge Sort", 1, draw_info.BLUE)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2 , 120))

    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg: # clear the background
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD, 
            draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val + 1) * draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]
        if i in color_positions:
            color = color_positions[i]
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()

def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst

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
 

def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)
    sorting = False
    ascending = True
    velocity = 60
    delay_time = 10

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(velocity) # changing the value from 120 to 60 will make it slower by a factor of 2
        pygame.time.delay(delay_time)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r: # click R to refresh the random lists
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            if event.key == pygame.K_RIGHT: # click rigth to add number refresh the random lists
                if n <= 90:
                    n += 10
                    delay_time -= 100 # decrease the delay time
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            if event.key == pygame.K_LEFT: # click left to decrease number refresh the random lists
                if n >= 30:
                    n -= 10
                    delay_time += 100 # increase the delay time
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and not sorting: # click SPACE to start sorting
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting: # click a to ascend
                ascending = True
            elif event.key == pygame.K_d and not sorting: # click d to descend
                ascending = False
            elif event.key == pygame.K_i and not sorting: # click i to insertion sort
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting: # click i to bubble sort
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_s and not sorting: # click i to selection sort
                sorting_algorithm = selection_sort
                sorting_algo_name = "Selection Sort"
            elif event.key == pygame.K_q and not sorting: # click q to quick sort
                sorting_algorithm = quick_sort
                sorting_algo_name = "Quick Sort"
            elif event.key == pygame.K_h and not sorting: # click h to heap sort
                sorting_algorithm = heap_sort
                sorting_algo_name = "Heap Sort"
            elif event.key == pygame.K_m and not sorting: # click m to merge sort
                sorting_algorithm = merge_sort
                sorting_algo_name = "Merge Sort"
            
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()







