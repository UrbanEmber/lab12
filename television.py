class Television:
    """A simple television simulator."""

    # Class constants
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initialize the television with default values."""
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__previous_volume = self.MIN_VOLUME  # Stores the last volume before muting

    def power(self) -> None:
        """Toggle the power status of the television."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle mute when the television is powered on. Muting saves and sets volume to 0; unmuting restores previous volume."""
        if self.__status:
            if not self.__muted:
                self.__previous_volume = self.__volume
                self.__volume = self.MIN_VOLUME
            else:
                self.__volume = self.__previous_volume
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel or loop back to the minimum channel if at maximum."""
        if self.__status:
            self.__channel = self.MIN_CHANNEL if self.__channel == self.MAX_CHANNEL else self.__channel + 1

    def channel_down(self) -> None:
        """Decrease the channel or loop back to the maximum channel if at minimum."""
        if self.__status:
            self.__channel = self.MAX_CHANNEL if self.__channel == self.MIN_CHANNEL else self.__channel - 1

    def volume_up(self) -> None:
        """Increase the volume, unmuting the TV if necessary."""
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume, unmuting the TV if necessary."""
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the TV's current settings as a string."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"


# Example usage
if __name__ == "__main__":
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.volume_up()
    print(tv)  # Expected output: Power = True, Channel = 1, Volume = 1