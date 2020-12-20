from src.area import * 
from src.volume import *


def test_list():
    assert [cubic(n) for n in range(2, 6)]==[8, 27, 64, 125]
    assert [rectangle(w, h) for w, h in [(1, 2), [5, 3]]]==[2, 15]