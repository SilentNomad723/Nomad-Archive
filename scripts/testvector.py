"""
Test vectors used during development.
"""

TEST_VECTORS = [
    {
        "input": [(0x01, 0x00), (0x02, 0x00), (0x03, 0x00), (0xFF, 0x00)],
        "output": "S"
    },
    {
        "input": [(0x01, 0x01), (0x02, 0x01), (0x03, 0x01), (0xFF, 0x01)],
        "output": "H"
    }
]


def validate(decode_fn):
    for vec in TEST_VECTORS:
        out = decode_fn(vec["input"])
        assert out == vec["output"], f"Mismatch: {out} != {vec['output']}"

    return True
