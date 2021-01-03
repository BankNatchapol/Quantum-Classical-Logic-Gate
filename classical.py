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
    return (bit1 + bit2) % 2


def xor_gate(bit1, bit2):
    assert bit1 in (0, 1) and bit2 in (0, 1), "Only 0 or 1"
    return int(bit1 != bit2)