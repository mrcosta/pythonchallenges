from codagem.codewars.arrays import merge

def test_merge_arrays():
    assert merge([1, 1, 1, 3, 4], [1, 2, 2, 5, 6]) == [1, 1, 1, 1, 2, 2, 3, 4, 5, 6]
