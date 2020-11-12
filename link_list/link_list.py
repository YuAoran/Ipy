# encoding=utf-8


# 链表
# 节点
class Node():

    def __init__(self,item):#节点初始条件有值
        self.item=item
        self.next=None

#创建链表的类
class SingleLink():
    #初始化，给定链表的头部属性
    def  __init__(self,node=None):
        self.__head=node

    #判断链表是否为空，即判断链表的head指针是否指向空
    def is_empty(self):
        return self.__head==None #为None返回True，不为None，False

    #判断链表的长度
    def length(self):
        if self.is_empty():
            return 0
        else:
            currentnode=self.__head     # 代表currentnode指向当前节点的游标与head指针指向同一个节点
            lengthcount=1   # 对比注释部分另一个方法，lengthcount=0
            while currentnode.next!=None:
                lengthcount+=1
                currentnode=currentnode.next
            return lengthcount

    #遍历整个链表
    def travel(self):
        if self.is_empty():
            return None
        else:
            allitemlist = []
            currentnode = self.__head
            allitemlist.append(currentnode.item)#先加入第一个
            while currentnode.next != None:
                currentnode = currentnode.next#尽管最后一个currentnode.next==None,但已经加入过
                allitemlist.append(currentnode.item)
            return allitemlist

    #链表头部加入元素
    def add(self,newitem):
        newnode = Node(newitem)
        if self.is_empty():
            self.__head = newnode
        else:
            newnode.next = self.__head
            self.__head = newnode

    #尾部添加元素,需要判断是否为空
    def append(self,newitem):
        newnode=Node(newitem)
        if self.is_empty():#类之间的函数调用用self.func
            self.__head = newnode
        else:
            currentnode=self.__head
            while currentnode.next!=None:
                currentnode=currentnode.next
            currentnode.next = newnode

    #指定位置添加元素，根据位置分为头部添加，尾部添加，中间位置添加，中间位置添加时需找到添加位置的前一个节点
    def insert(self,position,newitem):
        if position <=0:
            self.add(newitem)
        elif position >= self.length():#大于等于链表长度
            self.append(newitem)
        else:
            currentnode=self.__head
            positioncount=0
            newnode=Node(newitem)
            while positioncount<(position-1):#currentnode为插入位置前一个的节点
                currentnode=currentnode.next
                positioncount+=1
            newnode.next=currentnode.next
            currentnode.next=newnode

    #删除节点，再循环条件内查找
    def remove(self,item):
        currentnode = self.__head
        prenode = None
        while currentnode!=None:  # 判断是否找到
            if currentnode.item == item:  # 找到删除的值对应的节点
                if prenode == None:  # 如果前一个节点为空，则当前节点为第一个节点
                    self.__head = currentnode.next
                else:
                    prenode.next = currentnode.next
                break#注意break
            else:
                prenode = currentnode  # 将当前节点给前一个节点
                currentnode = currentnode.next  # 当前节点为其next的指向
        # 如果找到，判断curentnode是否为第一个节点

    #查找节点
    def search(self,item):
        currentnode=self.__head
        Found=False
        while not Found and currentnode!=None:#此处是currentnode，最后一个值也可找
            if currentnode.item==item:
                 Found=True
            else:
                currentnode=currentnode.next
        return Found

    #更新链表某个位置的值
    def update(self,position,newitem):
        if (position<0) or (position>self.length()):
            return False
        else:
            currentnode=self.__head
            positioncount=0
            while positioncount<position:
                currentnode=currentnode.next

                positioncount+=1
            currentnode.item=newitem

    #清空链表
    def clear(self):
        self.__head=None

