from collections import deque


def balanced_parentheses(string):

    # creating an empty stack using the python deque
    stack = deque()
    # append a default index - 1 to the stack
    stack.appendleft(-1)
    max_length = 0
    for i in range(len(string)):

        # check if the letter is an opening parentheses
        if string[i] == '(':
            stack.appendleft(i)
        else:
            # pop the topmost element
            stack.popleft()
            if len(stack) == 0:
                # if the stack is empty append the current index
                stack.appendleft(i)
            else:
                # current index is subtracted from the top element of the stack which is at index 0
                max_length = max(max_length, i-stack[0])

    return max_length


if __name__ == '__main__':
    assert balanced_parentheses('') == 0
    assert balanced_parentheses(' ') == 0
    assert balanced_parentheses('(') == 0
    assert balanced_parentheses(')') == 0
    assert balanced_parentheses('()(') == 2
    assert balanced_parentheses('())') == 2
    assert balanced_parentheses('())') == 2
    assert balanced_parentheses('(())') == 4
    assert balanced_parentheses('()()') == 4
    assert balanced_parentheses('(()()()(()') == 6
    assert balanced_parentheses('(()())') == 6
    assert balanced_parentheses('())(())') == 4
    assert balanced_parentheses('())(())') == 4
    assert balanced_parentheses(')(()))))((())(((()') == 4
    assert balanced_parentheses(')(()))))(((()') == 4
    assert balanced_parentheses('())((()))') == 6
    assert balanced_parentheses('()))(((()))') == 6
    assert balanced_parentheses('(()())((((()))))') == 16
