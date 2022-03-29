import area
def test_areaRec():
    x=5
    y=7
    result=area.area_rect(x,y)
    assert x*y==result

def test_periRec():
    x=5
    y=8
    result=area.perimeter_rect(x,y)
    assert x+x+y+y==result

def test_areaSquare():
    x=8
    result=area.area_square(x)
    assert x*x==result