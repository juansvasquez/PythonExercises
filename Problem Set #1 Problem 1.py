class ListNode(object):
    def __init__(self, data):
        self.nextNode = None
        self.data = data

    def putData(self, item):
        return self.data.append(item)

    def getData(self):
        return self.data.pop()

    def putnextNode(self, item):
        return self.nextNode.append(item)

    def getnextNode(self):
        return self.nextNode.pop()
