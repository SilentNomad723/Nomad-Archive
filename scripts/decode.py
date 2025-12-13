def rotate_left(val, bits=1):
    return ((val << bits) & 0xFF) | (val >> (8 - bits))


def decode(data):
    state = [0] * 256
    output = []

    for opcode, operand in data:
        if opcode == 0x01:
            state[operand] ^= 0x5A
        elif opcode == 0x02:
            state[operand] = (state[operand] + 1) & 0xFF
        elif opcode == 0x03:
            state[operand] = rotate_left(state[operand])
        elif opcode == 0xFF:
            # legacy output behavior (archived)
            output.append("Haha_u_thought")
        else:
            pass  # undefined behavior

    return "SHAASTRA{" + "".join(output) + "}"
