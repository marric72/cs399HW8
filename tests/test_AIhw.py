import cs399_HW8Marriott
import pytest

def test_test1():
	words=['apple', 'banana', 'mango', 'car']
	model = cs399_HW8Marriott.Load_Model()
	new_list = cs399_HW8Marriott.Sim_Check(model, words)
	assert new_list == ['apple', 'banana', 'mango']

def test_test2():
	words=['apple', 'banana', 'mango', 'car', 'pizza']
	model = cs399_HW8Marriott.Load_Model()
	new_list = cs399_HW8Marriott.Sim_Check(model, words)
	assert new_list == ['apple', 'banana', 'mango', 'pizza']

def test_test3():
	words=['apple', 'banana', 'mango', 'orange', 'car', 'bus', 'cherry']
	model = cs399_HW8Marriott.Load_Model()
	new_list = cs399_HW8Marriott.Sim_Check(model, words)
	assert new_list == ['apple', 'banana', 'mango', 'orange', 'cherry']

def test_all_same():
	"""All the words are same, remove nothing"""
	words=['cat','cat','cat']
	model = cs399_HW8Marriott.Load_Model()
	new_list = cs399_HW8Marriott.Sim_Check(model, words)
	assert new_list == words