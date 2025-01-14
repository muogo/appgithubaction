from src.oporation import add, kurang

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    
    
def test_kurang():
    assert kurang(5,3)==2
    assert kurang(4,1)==3
    assert kurang(5,2)==3
    assert kurang(1,3)==-2
    