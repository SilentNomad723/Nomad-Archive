#include <stdint.h>
#include <stddef.h>

/*
 * Experimental runtime loop.
 * Preserved for reference only.
 */

static uint8_t state[256];

void step(uint8_t opcode, uint8_t operand) {
    switch (opcode) {
        case 0x01:
            state[operand] ^= 0x5A;
            break;
        case 0x02:
            state[operand] += 1;
            break;
        default:
            break;
    }
}
