# Stack
def push(data):
	global SIZE, stack, top
	if top >= SIZE-1:
		print("Stack is full")
		return
	else:
		top += 1
		stack[top] = data

def pop():
	global SIZE, stack, top
	if top < 0:
		print("Stack is empty")
	else:
		print(stack[top])
		stack[top] = None
		top -= 1
	return

SIZE = 5
stack = ["0", "1", "2", "3", None]
top = 3
if __name__ == "__main__":
	print(stack)
	push("4")
	print(stack)
	push("5")
	pop()
	print(stack)
	pop()
	print(stack)
	pop()
	print(stack)
	pop()
	print(stack)
	pop()
	print(stack)
	pop()