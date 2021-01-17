# This is a sample Python script.
# Python 3.7.8
# https://daimhada.tistory.com/72 참고하기
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    # 마지막 삽입
    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            tempNode = self.head
            while tempNode.next is not None:
                tempNode = tempNode.next
            tempNode.next = node
        self.count += 1

    # 접근(인덱스로)
    def getdata(self, idx):
        if self.head is None:
            return 'no data in list'
        tempNode = self.head
        for i in range(idx):
            tempNode = tempNode.next
        return tempNode.data

    # 검색(데이터로)
    def getdataIndex(self, data):
        tempNode = self.head
        r_count = 0
        while tempNode is not None:
            if tempNode.data is data:
                break
            tempNode = tempNode.next
            r_count += 1

        # print('====test====')
        # print(tempNode)
        if tempNode is None:
            return 'null'
        else:
            return r_count

    # 임의 삽입
    def insertNodeAtIndex(self, idx, node):
        if idx < 0 or idx > self.count:
            return 'out of range'

        if idx is 0:
            node.next = self.head
            self.head = node
            return

        tempNode = self.head
        for i in range(idx - 1):
            tempNode = tempNode.next
        print('######' + str(tempNode.data))

        node.next = tempNode.next
        tempNode.next = node
        self.count += 1

    # 임의 노드 삭제
    def deleteAtIndex(self, idx):
        pass

    def print(self):
        print('count : ' + str(self.count))
        tempNode = self.head
        for i in range(self.count):
            print(tempNode.data)
            tempNode = tempNode.next


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('aaaa')
    s1 = SingleLinkedList()
    s1.append(Node(9))
    s1.append(Node(4))
    s1.append(Node(5))
    s1.append(Node(7))
    s1.append(Node(13))
    s1.append(Node(57))
    s1.append(Node(-3))
    s1.print()
    print(s1.getdata(2))        # 5
    print('============getdataIndex==============')
    print(s1.getdataIndex(-3))  # 4
    print('================count==================')
    print(s1.count)
    print('==========================')
    s1.insertNodeAtIndex(1, Node(8))
    s1.print()
    # print(s1.count)