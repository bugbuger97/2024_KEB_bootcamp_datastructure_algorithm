# Stack 응용 1

class Stack:
	def __init__(self):
		self.stack = list()
	def push(self, data):
		self.stack.append(data)
	def pop(self):
		print(self.stack[-1], end = "->")
		del(self.stack[-1])

if __name__ == "__main__":
	print("과자집에 가는 길 : ",end="")
	color = input().split("->")
	if color[-1] == "과자집":
		del(color[-1])
	s = Stack()
	for i in color:
		s.push(i)
	print("우리집에 오는 길 : ", end="")
	for i in range(len(s.stack)):
		s.pop()
	print("우리집")