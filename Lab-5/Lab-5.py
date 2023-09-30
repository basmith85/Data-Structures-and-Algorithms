class DisjointSet:
    def __init__(self, size):
        self.vertex = [i for i in range(size)]
        self.weight = [1] * size

    def validate(self, v1):
        if 0 <= v1 < len(self.vertex):
            return True
        else:
            return False
        
    def size(self, v1):
        if not self.validate(v1):
            raise ValueError("Invalid index")
        root = v1
        while root != self.vertex[root]:
            root = self.vertex[root]
        return self.weight[root]
    
    def parent(self, v1):
        if not self.validate(v1):
            raise ValueError("Invalid index")
        if self.weight[v1] < 0:
            return self.weight[v1]
        else:
            return self.vertex[v1]
        
    def isConnected(self, v1, v2):
        if not self.validate(v1) or not self.validate(v2):
            raise ValueError("Invalid index")
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 == root2:
            return True
        else:
            return False


    def find(self, v1):
        if not self.validate(v1):
            raise ValueError("Invalid index")
        while v1 != self.vertex[v1]:
            v1 = self.vertex[v1]
        return v1
    
    def unionByWeight(self, v1, v2):
        if not self.validate(v1) or not self.validate(v2):
            raise ValueError("Invalid index")
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.weight[root1] < self.weight[root2]:
                self.vertex[root1] = root2
                self.weight[root2] += self.weight[root1]
            else:
                self.vertex[root2] = root1
                self.weight[root1] += self.weight[root2]
    
    def unionByRank(self, v1, v2):
        if not self.validate(v1) or not self.validate(v2):
            raise ValueError("Invalid index")
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.weight[root1] < self.weight[root2]:
                self.vertex[root1] = root2
                self.weight[root2] += self.weight[root1]
            elif self.weight[root1] > self.weight[root2]:
                self.vertex[root2] = root1
                self.weight[root1] += self.weight[root2]
            else:
                self.vertex[root1] = root2
                self.weight[root1] += 1

    def joinBlocks(self, Connected):
        if not Connected:
            return None
        n = len(Connected)
        disjoint_set = DisjointSet(n)
        for i in range(n):
            for j in range(i + 1, n):
                if Connected[i][j] == 1:
                    disjoint_set.unionByWeight(i, j)
        return disjoint_set
    
    def findBlockSets(self):
        block_sets = set()
        n = len(self.vertex)
        for i in range(n):
            root = self.find(i)
            block_sets.add(root)
        return len(block_sets)
    
    def findBlockCount(self, blockid):
        if not self.validate(blockid):
            raise ValueError("Invalid")
        root = self.find(blockid)
        count = 0
        for i in range(len(self.vertex)):
            if self.find(i) == root:
                count += 1
        return count
    

if __name__ == '__main__':
  # Tasks A
  uf = DisjointSet(10)
  # 0 1-2-5-6-7 3-8-9 4
  uf.unionByRank(1, 2)
  uf.unionByRank(2, 5)
  uf.unionByRank(5, 6)
  uf.unionByWeight(6, 7)
  uf.unionByRank(3, 8)
  uf.unionByWeight(8, 9)
  print(uf.isConnected(1, 5))  # true
  print(uf.isConnected(5, 7))  # true
  print(uf.isConnected(4, 9))  # false
  # 0 1-2-5-6-7 3-8-9-4
  uf.unionByWeight(9, 4)
  print(uf.isConnected(4, 9))  # true
  

  # Tasks B
  Connected = [[1,1,0,1], [1,1,0,0], [0,0,1,1], [1,0,1,1]]
  uf = DisjointSet(4)
  uf.joinBlocks(Connected)
  uf.findBlockCount(1)
  print(uf.findBlockCount(1))
