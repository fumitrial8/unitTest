import pytest
from run import hello_world

texts = ["Hello World!","Hello World","Hello Wrld!"]

@pytest.mark.parametrize('res', texts)
def test_helloworld(res):
    assert res == "Hello World!"


@pytest.mark.xfail()
def test_helloworld_fail():
    res = hello_world()
    assert res == "Hello Wrld!"