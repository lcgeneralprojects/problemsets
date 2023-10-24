# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.current = -1
        self.data = []
        for element in nestedList:
            if element.isInteger():
                self.data.append(element.getInteger())
            else:
                tmp = NestedIterator(element.getList())
                while tmp.hasNext():
                    self.data.append(tmp.next())


    def next(self) -> int:
        self.current += 1
        return self.data[self.current]

    def hasNext(self) -> bool:
        return self.current+1 < len(self.data)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
