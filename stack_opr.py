stack = []

def push(item):
    stack.append(item)
    print(f"{item} pushed into stack")

def pop():
    if is_empty():
        print("Stack Underflow")
        return None
    return stack.pop()

def peek():
    if is_empty():
        print("Stack is empty")
        return None
    return stack[-1]

def is_empty():
    return len(stack) == 0

def size():
    return len(stack)

# Demo
push(10)
push(20)
push(30)
print("Top:", peek())
print("Popped:", pop())
print("Size:", size())
print("Is Empty:", is_empty())
