#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
	"""prints a matrix of integers"""
	for _ in range(len(matrix)):
		if len(matrix[_]) == 0:
			print('')
			continue
		for i in range(len(matrix[_])):
			if i == (len(matrix[_]) - 1):
				print("{}".format(matrix[_][i]))
				continue
			print("{}".format(matrix[_][i]), end=' ')
