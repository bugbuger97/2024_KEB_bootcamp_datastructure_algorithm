# Stack 응용 1

class Stack:
	def __init__(self):
		self.stack = list()
	def push(self, data):
		self.stack.append(data)
	def pop(self):
		print(self.stack[-1],end="")
		del(self.stack[-1])

if __name__ == "__main__":
	string = """
	진달래꽃
	나 보기가 역겨워
	가실 때에는
	말 없이 고이 보내드리오리다.
	"""
	print("----------- 원본 -----------")
	print(string)
	print("----------- 결과 -----------")
	s = Stack()
	for i in string:
		s.push(i)
	for i in range(len(s.stack)):
		s.pop()