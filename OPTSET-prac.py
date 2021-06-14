class Node:
	def __init__(self, data):
		self.data = data
		self.left = None 
		self.right = None
class Trie:
	def __init__(self):
		self.root = Node(0)
	def insert(self, pre_xor):
		self.temp = self.root
		for i in range(31, -1, -1):
			val = pre_xor & (1<<i)
			if val :
				if not self.temp.right:
					self.temp.right = Node(0)
				self.temp = self.temp.right
			if not val:
				if not self.temp.left:
					self.temp.left = Node(0)
				self.temp = self.temp.left
		self.temp.data = pre_xor

	def query(self, xor):
		self.temp = self.root
		for i in range(31, -1, -1):
			val = xor & (1<<i)
			if val:
				if self.temp.left:
					self.temp = self.temp.left
				elif self.temp.right:
					self.temp = self.temp.right
			else:
				if self.temp.right:
					self.temp = self.temp.right
				elif self.temp.left:
					self.temp = self.temp.left

		return xor ^ self.temp.data

	def maxSubArrayXOR(self, n, Arr,k):
		self.insert(0)
		ans=[]
		result = -float('inf')
		pre_xor = 0
		for i in range(n):
			pre_xor = pre_xor ^ Arr[i]
			self.insert(pre_xor)
			if(self.query(pre_xor)>result):
				result=self.query(pre_xor)
				ans.append(Arr[i])
		return ans


if __name__ == "__main__":
	for i in range(int(input())):
		n,k=map(int, input().split()) 
		arr=list(range(1, n+1))
		trie = Trie()
		print(trie.maxSubArrayXOR(n, arr,k))



	