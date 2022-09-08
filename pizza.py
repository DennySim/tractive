h1 = [1, 2, 1, 1]
h2 = [1, 1, 2]
h3 = [1, 1]

stacks = [h1, h2, h3]

def get_stack_height(stack):
    return sum(stack)


def create_stack_height_list(stacks):
    stack_sizes = []
    for h, stack in enumerate(stacks):
        stack_sizes.append(get_stack_height(stack))
    return stack_sizes


def get_max_stack_height(stacks):
    stack_sizes = create_stack_height_list(stacks)
    max_stack_height_value = max(stack_sizes)
    max_stack_height_index = stack_sizes.index(max_stack_height_value)

    return max_stack_height_index, max_stack_height_value


def is_same_height(stacks):
    if len(set(create_stack_height_list(stacks))) <= 1:
        return True


def pizza_eating(stacks):

    #stacks = stacks

    if is_same_height(stacks):
        return get_stack_height(stacks[0])

    while len(set(create_stack_height_list(stacks))) > 1:

        # Step 1. find heightest stack (no matter if there are more than one heightest stack)
        max_stack_height = get_max_stack_height(stacks)

        # Step 2. eating pizza from heightest stack
        # max_stack_height is tuple(stack_index, stack_height)
        del stacks[max_stack_height[0]][0]

        if is_same_height(stacks):
            return get_stack_height(stacks[0])


pizza_eating(stacks)

# OUTPUT FOR CHECK
#def main():
#    print(pizza_eating(stacks))
#main()