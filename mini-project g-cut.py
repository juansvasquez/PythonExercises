class DictionaryNode:
        def __init__(self, k, v):
                self.key = k
                self.value = v
                self.next = None
        def getKey(self):
                return self.key
        def setKey(self, newk):
                self.key = newk
        def getValue(self):
                return self.value
        def setValue(self, newv):
                self.value = newv
        def getNext(self):
                return self.next
        def setNext(self, newn):
                self.next = newn        
        def __str__(self):
                return  str(self.key) + ":" + str(self.value)

class LinkedList:
        def __init__(self):
                self.front = None
        def putFront(self, k, v):
                n = DictionaryNode(k, v)
                if self.front== None:
                        self.front = n
                else:
                        n.setNext(self.front)
                        self.front = n
        def __str__(self):
                s = ""
                cn= self.front
                while cn != None:
                        s += str(cn)
                        s+= " --> "
                        cn = cn.getNext()
                s+="None"
                return s
        def search(self, target):
                #Returns a DictionaryNode in the list if its key is equal to target. 
                ##Will return None if target is not one of the keys in the Linked List
                cn = self.front 
                while cn != None and cn.getKey() != target:
                        cn = cn.getNext()
                return cn

class HashTable(object):
        def __init__(self, numBuckets):
                self.buckets = []
                self.numBuckets = numBuckets
                ll = LinkedList()
                for i in range(numBuckets):
                        self.buckets.append(ll)
        def hashFunction(self, s):
                sum = 0
                for i in range(len(s)):
                        sum += ord(s[i])
                return sum%self.numBuckets
        def __str__(self):
                return str(self.buckets) 
        def __setitem__(self, key, value):
                self.buckets[self.hashFunction(key)] = value
        def __getitem__(self, key):
                return self.buckets[self.hashFunction(key)]
        

def testDictionaryNode():
        d = DictionaryNode("Hello",10)
        print(d)
        print(d.getKey())
        print(d.getValue())
        d.setKey("Goodbye")
        print(d)
        d.setValue(1)
        print(d)
        print(d.getNext())
        d2 = DictionaryNode("HelloAgain",10)
        d.setNext(d2)
        print(d.getNext())

def testLinkedList():
        d = LinkedList()
        print(d)
        print(d.search("Yellow"))
        d.putFront("Hello",1)
        print(d)
        print(d.search("Hello"))
        d.putFront("Goodbye", 99)
        print(d)
        print(d.search("Hello"))
        print(d.search("Yo"))

def testHashTable():
        d = HashTable(20)
        d["hey what's up"]=92
        d["OOPS14"]=45
        d["yolo"]=13
        d["bhsec"]=82
        print(d["OOPS14"])
        print(d["bhsec"])
        d["bhsec"]=99
        print(d)
        print(d["bhsec"])
        print(d["bhsecq"])

testDictionaryNode()
testLinkedList()
testHashTable()
