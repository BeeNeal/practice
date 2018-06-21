#!usr/bin/env python

from Queue import PriorityQueue

# priorityqueue is similar to dictionary of lists


class State(object):

    def __init__(self, value, parent,
                 start=0, goal=0):
            # defaults for start state only, otherwise can grab data from parent
        self.children = []  # children are all neighboring possibilities
        self.parent = parent
        self.value = value
        self.dist = 0

        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:  # if there is no parent
            self.path = [value]
            self.start = start
            self.goal = goal

    def GetDist(self):
        pass

    def CreateChildren(self):
        pass

class StateString(State):
    def __init__(self, value, parent, start=0, goal=0):
        super(StateString, self).__init__(value, parent, start, goal)
        self.dist = self.GetDist()

    def GetDist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            # find dist from letter and target placement
            dist += abs(i - self.value.index(letter))
        return dist

    def CreateChildren(self):
        if not self.children:
            for i in xrange(len(self.goal) - 1):
                val = self.value
                val = val[:i] + val[i + 1] + val[i] + val[i + 2]
                child = StateString(val, self)
                self.children.append(child)


class AStarSolver():
    def __init__(self, start, goal):
        self.path = []  # saves final solution from s to e state
        self.visitedQueue = []  # keeps track of all visited children, so don't get caught in loop
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def Solve(self):
        startState = StateString(self.start, 0, self.start, self.goal)
        count = 0  # increments per child created
        self.priorityQueue.put((0, count, startState))
        while(not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2]  # get top most valued state from P Queue
            closestChild.CreateChildren()
            self.visitedQueue.append(closestChild.value)
            # if the child not visited,
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count += 1
                    if not child.dist:  # if still haven't found path, no more children
                        self.path = child.path
                        break
                        self.priorityQueue.put((child.dist, count, child))
        # error handling
        if not self.path:
            print "Goal of" + self.goal + "not possible"
            return self.path 

if __name__ == '__main__':
    start1 = "cdabfe"
    goal1 = 'abcdef'
    print "starting..."
    a = AStarSolver(start1, goal1)
    a.Solve()
    for i in xrange(len(a.path)):
        print "%d) " %i + a.path[i]