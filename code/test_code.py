def get_max(values):
	"""
	A simple function to get maximum value from a list of values
	"""

	max_value = values[0]

	for value in values[1:]:
		if value > max_value:
			max_value = value

	return max_value

# Execute with py.test or similar
def test_get_max():

    values = [2, 5, 10, 1]

    expected = 10
    actual = get_max(values)

    assert expected == actual