def rgb_to_hex(r: int, g: int, b: int) -> str:
    """

    :param r: Red value (0 - 255)
    :param g: Green value (0 - 255)
    :param b: Blue value (0 - 255)
    :return: Hex color as a string (#XXXXXX)
    """
    return "#{0:02x}{1:02x}{2:02x}".format(r, g, b)


# Filler text
LOREM_IPSUM: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt "
