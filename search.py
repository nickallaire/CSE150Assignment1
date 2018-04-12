# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
"""
    '''print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())'''

    "*** YOUR CODE HERE ***"
    # use stack as data structure
    stack = util.Stack()
    successors = problem.getSuccessors(problem.getStartState())

    # parent map is used to determine the path to the goal
    parentMap = {}
    parentMap[problem.getStartState] = 0

    # count is used to determine if a node had been visited before
    count = util.Counter()

    # actions is the list of actions to take to reach the goal
    actions = []
    count[problem.getStartState()] += 1

    #add start states successors to stack
    while len(successors) > 0 :
        suc = successors.pop(0)
        if count[suc[0]] == 0 :
            stack.push(suc)
            #count[suc[0]] += 1
            parentMap[suc] = 0

    #DFS algorithm
    while (stack.isEmpty() != 1):
        nextMove = stack.pop()
        count[nextMove[0]] += 1
        if problem.isGoalState(nextMove[0]) == True:
            currNode = nextMove
            while (currNode != 0) :
                actions.insert(0, currNode[1])
                currNode = parentMap[currNode]
            return actions
        else:
            newSuccessors = problem.getSuccessors(nextMove[0])
            while len(newSuccessors) > 0:
                sucToAdd = newSuccessors.pop(0)
                if count[sucToAdd[0]] == 0:
                    stack.push(sucToAdd)
                    parentMap[sucToAdd] = nextMove


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # use queue as data structure
    queue = util.Queue()
    successors = problem.getSuccessors(problem.getStartState())

    # parent map is used to determine the path to the goal
    parentMap = {}
    parentMap[problem.getStartState] = 0

    # count is used to determine if a node had been visited before
    count = util.Counter()

    # actions is the list of actions to take to reach the goal
    actions = []
    count[problem.getStartState()] += 1

    #add start states successors to queue
    while len(successors) > 0:
        suc = successors.pop(0)
        if count[suc[0]] == 0:
            queue.push(suc)
            count[suc[0]] += 1
            parentMap[suc] = 0

    #BFS algorithm
    while(queue.isEmpty() != 1) :
        nextMove = queue.pop()
        if problem.isGoalState(nextMove[0]) == True:
            if count[nextMove[0]] > 0:
                currNode = nextMove
                while (currNode != 0):
                    actions.insert(0, currNode[1])
                    currNode = parentMap[currNode]
                return actions
        else:
            newSuccessors = problem.getSuccessors(nextMove[0])
            while len(newSuccessors) > 0:
                sucToAdd = newSuccessors.pop(0)
                if count[sucToAdd[0]] == 0:
                    queue.push(sucToAdd)
                    parentMap[sucToAdd] = nextMove
                    count[sucToAdd[0]] += 1



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # use priority queue as data structure
    pqueue = util.PriorityQueue()
    successors = problem.getSuccessors(problem.getStartState())

    # parent map is used to determine the path to the goal
    # valueParentMap is used to determine the total cost to reach the node
    parentMap = {}
    valueParentMap = {}
    parentMap[problem.getStartState()] = 0
    valueParentMap[problem.getStartState()] = 0

    # count is used to determine if a node had been visited before
    count = util.Counter()

    # actions is the list of actions to take to reach the goal
    actions = []
    count[problem.getStartState()] += 1

    #add start states successors to priority queue
    while len(successors) > 0:
        suc = successors.pop(0)
        if count[suc[0]] == 0:
            pqueue.push(suc, suc[2])
            count[suc[0]] += 1
            parentMap[suc] = 0
            valueParentMap[suc[0]] = suc[2]

    #UCS algorithm
    while (pqueue.isEmpty() != 1):
        nextMove = pqueue.pop()
        if problem.isGoalState(nextMove[0]) == True:
            if count[nextMove[0]] > 0:
                currNode = nextMove
                while (currNode != 0):
                    actions.insert(0, currNode[1])
                    currNode = parentMap[currNode]
                return actions
        else:
            newSuccessors = problem.getSuccessors(nextMove[0])
            while len(newSuccessors) > 0:
                sucToAdd = newSuccessors.pop(0)
                if count[sucToAdd[0]] == 0 or sucToAdd[2] + valueParentMap[nextMove[0]] < valueParentMap[sucToAdd[0]] :
                    pqueue.push(sucToAdd, sucToAdd[2] + valueParentMap[nextMove[0]])
                    valueParentMap[sucToAdd[0]] = sucToAdd[2] + valueParentMap[nextMove[0]]
                    parentMap[sucToAdd] = nextMove
                    count[sucToAdd[0]] += 1



    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # use priority queue as data structure
    pqueue = util.PriorityQueue()
    successors = problem.getSuccessors(problem.getStartState())

    # parent map is used to determine the path to the goal
    # valueParentMap is used to determine the total cost to reach the node
    parentMap = {}
    valueParentMap = {}
    parentMap[problem.getStartState()] = 0
    valueParentMap[problem.getStartState()] = 0

    # count is used to determine if a node had been visited before
    count = util.Counter()

    # actions is the list of actions to take to reach the goal
    actions = []
    count[problem.getStartState()] += 1

    #add start states successors to priority queue
    while len(successors) > 0:
        suc = successors.pop(0)
        if count[suc[0]] == 0:
            pqueue.push(suc, suc[2] + heuristic(suc[0], problem))
            count[suc[0]] += 1
            parentMap[suc] = 0
            valueParentMap[suc[0]] = suc[2]

    #A* Search algorithm
    while (pqueue.isEmpty() != 1):
        nextMove = pqueue.pop()
        if problem.isGoalState(nextMove[0]) == True:
            if count[nextMove[0]] > 0:
                currNode = nextMove
                while (currNode != 0):
                    actions.insert(0, currNode[1])
                    currNode = parentMap[currNode]
                return actions
        else:
            newSuccessors = problem.getSuccessors(nextMove[0])
            while len(newSuccessors) > 0:
                sucToAdd = newSuccessors.pop(0)
                if count[sucToAdd[0]] == 0 or sucToAdd[2] + valueParentMap[nextMove[0]] < valueParentMap[sucToAdd[0]] :
                    pqueue.push(sucToAdd, sucToAdd[2] + valueParentMap[nextMove[0]] + heuristic(nextMove[0], problem))
                    valueParentMap[sucToAdd[0]] = sucToAdd[2] + valueParentMap[nextMove[0]]
                    parentMap[sucToAdd] = nextMove
                    count[sucToAdd[0]] += 1

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
