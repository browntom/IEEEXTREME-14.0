class BinaryTreenode:


  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


  def add_child(self, data):


        if data==self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinaryTreenode(data)
        else:
             if self.right:
                 self.right.add_child(data)
             else:
                 self.right =BinaryTreenode(data)



if __name__ =='__main__':
    x = int(input())
    numberlist = [int(x) for x in input().split()]
    root =BinaryTreenode( numberlist[0])
    output = []
    print(1, end=' ')

    for number in numberlist[1:]:
        current_Node = root
        distance = 1
        while True:
            distance += 1
            if number> current_Node.data:
                if current_Node.right == None:
                    current_Node.right = BinaryTreenode(number)
                    print(distance, end=' ')
                    break
                current_Node = current_Node.right
            else:
                if current_Node.left == None:
                    current_Node.left = BinaryTreenode(number)
                    print(distance, end=' ')
                    break
                current_Node = current_Node.left
    print()





