"""Some basic asserts to check all is wired up"""

from time import sleep
import pytest
from rich.console import Console

console = Console()


def test_0001_SET_pass():
    console.print("\n[blue bold]Testing add function...[/]\n")
    assert 1+ 4 == 5


# A test that is expected to fail so xfail will give a 'pass'
@pytest.mark.xfail
def test_0002_SET_xfail():
    assert 0


# A test that was expected to fail but passes so is an xpass
@pytest.mark.xfail
def test_0003_SET_xpass():
    sleep(1)
    assert True


# A test fail to show as an example
@pytest.mark.skip
def test_0004_SET_this_will_fail():
    console.print("[red italic]Example of a failed test[/]⚠️")
    assert 3 * 2 == 5


# A test to show we can have many markers and their order
@pytest.mark.sanity
@pytest.mark.outer
@pytest.mark.setup
@pytest.mark.inner
def test_0005_SET_many_markers():
    assert 1 in divmod(9, 5)
    assert "this" in "this is pytest"
    assert [1, 2, 4] == [1, 2, 4]


# A test using pytest.raises
@pytest.mark.sanity
def test_0006_SET_case01():
    console.print("[dark_orange bold italic]Example output pytest.raises passes[/]")
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0


# A test with skip and optional reason
@pytest.mark.skip(reason="data not ready")
def test_0007_SET_skip():
    assert True


# Raise a ValueError
def myfunc():
    print("\n\tmyfunc ValueError")
    raise ValueError("Exception 123 raised")


def test_0008_SET_match_raises():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()


@pytest.mark.parametrize("n, expected", [(1, 2), (3, 4)])
class TestClassSetup:
    def test_0009_SET_simple_case(self, n, expected):
        assert n + 1 == expected
