import pytest

from numrange import closedrange

# def test_fail():
#     assert pytest.fail("これは失敗するはず")


@pytest.fixture(scope="module")
def closed_range_positive():
    return closedrange(3, 20)


@pytest.fixture(scope="module")
def closed_range_negative():
    return closedrange(-10, -3)


class TestVerifyRange:
    class TestNumInRange:
        def test_positive_range(self, closed_range_positive):
            assert closed_range_positive.isin(10)

        def test_negative_range(self, closed_range_negative):
            assert closed_range_negative.isin(-8)

    class TestNumOutRange:
        def test_positive_range(self, closed_range_positive):
            assert not closed_range_positive.isin(1)

        def test_negative_range(self, closed_range_negative):
            assert not closed_range_negative.isin(-12)

    class TestNumOnRange:
        def test_positive_range(self, closed_range_positive):
            assert closed_range_positive.isin(3)
            assert closed_range_positive.isin(20)

        def test_negative_range(self, closed_range_negative):
            assert closed_range_negative.isin(-10)
            assert closed_range_negative.isin(-3)


class TestConvertStr:
    def test_positive_range(self, closed_range_positive):
        assert closed_range_positive.to_str() == "[3, 20]"

    def test_negative_range(self, closed_range_negative):
        assert closed_range_negative.to_str() == "[-10, -3]"


class TestVerifyNum:
    class TestReverseOrder:
        def test_positive_range(self):
            with pytest.raises(ValueError):
                closedrange(10, 3)

        def test_negative_range(self):
            with pytest.raises(ValueError):
                closedrange(-3, -10)
