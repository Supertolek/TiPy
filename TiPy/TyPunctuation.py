class Punctuation:
	lowercase = "abcdefghijklmnopqrstuvwxyz"
	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	variables = lowercase + uppercase

	# Operators
	plus = ["+"]
	minus = ["-"]
	multiply = ["*"]
	divide = ["/"]
	equals = ["="]
	operators = plus + minus + multiply + divide + equals

	# Single letter
	functionEnter = ["<"]
	functionExit = [">"]
	functionContentEnter = ["("]
	functionContentExit = [")"]
	controlBodyEnter = ["{"]
	controlBodyExit = ["}"]
	classChildren = ["."]

	# List/matrix
	listEnter = ["["]
	listExit = ["]"]

	# String
	stringDelimiter = ["\"", "'"]

	# Arguments
	argumentsDelimiter = [","]

	# Comment
	singleLineComment = ["//", "#"]
	multiLineCommentEnter = ["/*"]
	multiLineCommentExit = ["*/"]

def contains(contener, contained):
	if type(contained) == str:
		return contained in contener
	elif type(contained) == list:
		for toCheck in contained:
			if toCheck in contener:
				return True
		return False
	else:
		return False