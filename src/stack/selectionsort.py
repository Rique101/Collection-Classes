from node.node import *
from stack.stack import *

def selectionsort(data: stack, first: int):
    i = data.size() - first - 1

    while i > 0:
        big = first
        j = first + 1

        while j <= first + i:
            if data.peek()[node.listPosition(data.getHead(), i+big)] < data.peek()[j]:
                big = j
            j += 1

        temp = data.pop()[first + i]
        data.push(temp)

        # Set the data at the specified position
        cursor = data.peek()
        cursor.setDataAtPosition(first + i, temp)

        i -= 1


