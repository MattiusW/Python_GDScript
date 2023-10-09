def main():
    stack = []
    push("Baldur's Gate 3", stack)
    push("Rage2", stack)
    print(stack)
    print(emptyStack(stack))
    print(sizeStack(stack))
    pop(stack)
    print(stack)
    pop(stack)
    print(stack)
    print(emptyStack(stack))
    print(sizeStack(stack))
    pop(stack)
    

def push(element, stacks):
    stacks.append(element)

def pop(stacks):
    if (emptyStack(stacks) == False):
        del stacks[-1]
    else:
        print("This is not happen")

def sizeStack(stacks):
    amount = 0
    for i in range(len(stacks)):
        amount += 1
    return amount

def emptyStack(stacks):
    if (len(stacks) == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    main()