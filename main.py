"""
Input and output file creation functions and main part are implemented in this file.
To run, just type "python3 main.py" into the Console.
"""
import sys
from state import State
from typing import Tuple, List
from idastar import ida_star
from RBFS_search import recursive_best_first_search
from puzzle import Puzzle

def take_input() -> State:
    with open('input.txt', 'r') as input_file:
        goal: List[Tuple[int, int, int]] = []
        for _ in range(3):
            goal.append(tuple(map(lambda x: int(x), input_file.readline().split())))

        input_file.readline()

        initial: List[Tuple[int, int, int]] = []
        for _ in range(3):
            initial.append(tuple(map(lambda x: int(x), input_file.readline().split()))
                           )
    return State(initial, goal)

def take_input_for_rbfs():
    with open('input.txt', 'r') as input_file:
        list_init_1=list(map(lambda x: int(x), input_file.readline().split()))
        list_init_2=list(map(lambda x: int(x), input_file.readline().split()))
        list_init_3=list(map(lambda x: int(x), input_file.readline().split()))
        initial=[list_init_1+list_init_2+list_init_3]
        print(initial)
        input_file.readline()
        list_goal_1=list(map(lambda x: int(x), input_file.readline().split()))
        list_goal_2=list(map(lambda x: int(x), input_file.readline().split()))
        list_goal_3=list(map(lambda x: int(x), input_file.readline().split()))
        goal=list_goal_1+list_goal_2+list_goal_3
        return [initial,goal]


if __name__ == '__main__':
    print('Running...')
    state: State = take_input()
    sys.stdout = open('outputIDA.txt', 'w')
    res = ida_star(state)
    if res is None:
        print('fail')
    print("------------------------------------------------------")
    Puzzle.num_of_instances = 0
    RBFS = recursive_best_first_search(take_input_for_rbfs()[0])
    print('RBFS:',RBFS)
    print('space:', Puzzle.num_of_instances)
    print()

    print('------------------------------------------')
