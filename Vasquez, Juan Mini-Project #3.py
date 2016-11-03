class DictionaryNode(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.nextNode = None
    def __str__(self):
        return str(DictionaryNode().getKey()) + ":" + str(DictionaryNode().getValue())
    def getKey(self):
        return self.key
    def getValue(self):
        return self.value
    def getNext(self):
        return self.nextNode
    def setKey(self, newKey):
        self.key = newKey
    def setValue(self, newValue):
        self.value = newValue
    def setNext(self, newNextNode):
        self.nextNode = newNextNode
class LinkedListDictionary(object):
    def __init__(self):
        self.numNodes = 0
        self.startNode = None
    def __getitem__(self, key):
        if self.numNodes == 0:
            return None
        cn = self.startNode
        for k in range(self.numNodes):
            if key == cn.getKey():
                return cn.getValue()
            elif cn.getNext() == None:
                return None
            else:
                cn = cn.getNext()
    def __setitem__(self, key, value):
        n = DictionaryNode(key, value)
        if self.numNodes == 0:
            self.startNode = n
            self.numNodes += 1
        elif LinkedListDictionary()[key] == None:
            cn = self.startNode
            while cn.getNext() != None:
                cn = cn.getNext()
            cn.setNext(n)
            self.numNodes += 1
        else:
            LinkedListDictionary()[key] = value
    def __str__(self):
        cn = self.startNode
        s = ""
        while cn != None:
            s += cn.__str__()
            s += "->"
            cn = cn.getNext()
        s += "None"
        return s

#TEST CODE ENGAGED
d = LinkedListDictionary()
d["hey what's up"]=92
d["OOPS14"]=45
d["yolo"]=13
d["bhsec"]=82
print(d["OOPS14"])
print(d["bhsec"])
d["bhsec"]=99
#print(d)
print(d["bhsec"])
print(d["bhsecq"])
