#!/usr/bin/python3

"""
Module for validating UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validate if the given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if data is valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0
    for byte in data:
        # Determine the number of bytes in the current UTF-8 character
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character
            elif (byte >> 7):
                return False  # Invalid start byte
        else:
            # Check if byte is a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0  # Ensure all characters are complete
