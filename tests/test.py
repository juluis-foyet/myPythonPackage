from mypackage import myModule

def test_top_n():
    """
    Makes sure top_n() function works properly
    """

    assert myModule.top_n([1,2,3,4,5], 2) == [4,5], 'incorrect'
    assert myModule.top_n([12,13,14,15], 3) == [13,14,15], 'incorrect'
    assert myModule.top_n([50,60,90,80], 2) == [80,90], 'incorrect'