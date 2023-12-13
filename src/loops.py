@staticmethod
def evens (start: int, end: int):
    """Finds and displays the even numbers between a specified
    starting and ending value.
    Args:
    start (int): specified starting value
    end (int): specified ending value
    """
    i = start
    while (i <= end):
        if (i % 2 == 0):
            print(i, end=" ")
        i += 1


#Recursion
@staticmethod
def evens_recursive(start: int, end: int):
    if start > end:
        return
    if start % 2 == 0:
        print(start, end=" ")
    evens_recursive(start + 1, end)
