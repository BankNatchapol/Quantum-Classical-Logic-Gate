def not_gate(bit):
    assert bit in (0, 1), "Only 0 or 1"
    if bit:
        return 0
    return 1


def and_gate(bit1, bit2):
    assert bit1 in (0, 1) and bit2 in (0, 1), "Only 0 or 1"
    return bit1 * bit2


def or_gate(bit1, bit2):
    assert bit1 in (0, 1) and bit2 in (0, 1), "Only 0 or 1"
    if 1 in (bit1, bit2):
        return 1
    return 0


def xor_gate(bit1, bit2):
    assert bit1 in (0, 1) and bit2 in (0, 1), "Only 0 or 1"
    if bit1 != bit2:
        return 1
    return 0
