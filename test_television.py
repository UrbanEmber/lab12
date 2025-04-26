import pytest
from television import Television  # Import the Television class


@pytest.fixture
def tv():
    """Create a new Television instance for testing."""
    return Television()


def test_init(tv):
    """Test initial values of the Television."""
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power(tv):
    """Test power functionality."""
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_mute(tv):
    """Test mute functionality."""
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_channel_up(tv):
    """Test channel increase functionality."""
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  # Should wrap around to MIN_CHANNEL
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down(tv):
    """Test channel decrease functionality."""
    tv.power()
    tv.channel_down()  # Should wrap around to MAX_CHANNEL
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"


def test_volume_up(tv):
    """Test volume increase functionality."""
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_up()
    tv.volume_up()  # Should stay at MAX_VOLUME
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down(tv):
    """Test volume decrease functionality."""
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_down()
    tv.volume_down()  # Should stay at MIN_VOLUME
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


if __name__ == "__main__":
    pytest.main()
