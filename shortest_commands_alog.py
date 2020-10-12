"""
@Haris Muzaffer
This algorithm accepts a Number N and returns shortest sequence of commands required to set either L or R to the given number N.
It constructs a binary tree in level order fashion with the help of a queue data structure.
Each Node of the tree saves value of L and R and also saves the command 'L' or 'R' that was performed.
Node also saves the reference to previous/parent Node and references to left and right child of the Node.

This binary tree continues to build until the condition L = N or R = N is met. Once the condition are met, the function
returns and calculates the path from the Node where the conditions were met upto the first command

The program also takes care whether applying command L or R would make sense and case of not meeting the conditions
L = N or R = N
"""

from collections import deque


class Node:                                    #Node class

    def __init__(self, l, r, command, pre):  #'l' is the value of integer 'L' and 'r' is the value of integer'R'

        self.l = l
        self.r = r
        self.command = command              #command : 'L' or 'R'
        self.left = None;                   #left references the left child and right references the right child
        self.right = None;
        self.pre = pre;                     #pre saves the previous Node/ parent reference


class Mammoth:

    def __int__(self):
        print()

    def solution(self, n):        #this method constructs a binary tree in level order fashion using a queue

        while True:

            if not queue:                   #initially queue will have one element i.e. root Node, then once it is
                return "impossible"         #empty, that means conditions L = N or R = N can not be met anymore

            pre = queue.popleft()

            left = Node(2 * pre.l - pre.r, pre.r, 'L', pre)     #create left Node with L changed to 2 * L - R
            if left.l == n or left.r == n:                      #if conditions L = N or R = N are met, return
                return self.shortest_sequence(left)

            if (abs((n - pre.l)) >= abs(n - left.l)) or abs(n - left.r) >= abs(n - (2 * left.r - left.l)):
                #this logic says: attach the left Node only if the possibility of conditions L = N or R = N is there
                pre.left = left
                queue.append(left)

            right = Node(pre.l, 2 * pre.r - pre.l, 'R', pre)    #create right Node with L changed to 2 * R - L
            if right.l == n or right.r == n:                    #if conditions L = N or R = N are met, return
                return self.shortest_sequence(right)

            if (abs((n - pre.r)) >= abs(n - right.r)) or abs(n - right.l) >= abs(n - (2 * left.l - right.r)):
                # this logic says: attach the right Node only if the possibility of conditions L = N or R = N is there
                pre.right = right
                queue.append(right)


    def shortest_sequence(self, node):      #this method returns the shortest sequence

        cnode = node
        command_string = [cnode.command]

        while True:

            if cnode.pre.command == 'O':
                break

            command_string.append(cnode.pre.command)
            cnode = cnode.pre;

        command_string.reverse()
        return command_string


#driver code
mammoth = Mammoth()
root = Node(0, 1, 'O', None)        #create initial Node with 'L'= 0, 'R'= 1, command = 'O'(dummy command to start)
queue= deque()
queue.append(root)                  #append the root Node to the queue
n= int(input("Enter the number"))
shortest_sequence = mammoth.solution(n)
for path in shortest_sequence:
    print(path, end="")