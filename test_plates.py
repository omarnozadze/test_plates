from plates import is_valid


def test_number():
    assert is_valid ("22223")== False
    assert is_valid("!@#$%")==False

def test_words_six():
    assert is_valid ("12367sss") == False

def test_zero():
    assert is_valid ("0h1ll")== False


def test_plates():
    assert is_valid('IO') == True
    assert is_valid('HELLO') == True
    assert is_valid('HE0') == True   
    
def test_invalid_alaphabet():
    assert is_valid('H@E234!') == False 