from collections import namedtuple
from math import ceil

Packet = namedtuple("Packet", ["version", "type", "values"])

def parse(puzzle_input):
    line = puzzle_input[0]
    bits = bin(int(line, 16))[2:]
    size = len(bits)
    bits = bits.zfill(ceil(size/8)*8)
    return bits

def read(bits):
    packets = list()

    version, bits = int(bits[:3], 2), bits[3:]
    packet_type, bits = int(bits[:3], 2), bits[3:]

    values = list()
    if packet_type == 4:
        value = ""
        while True:
            raw, bits = bits[:5], bits[5:]
            rtype, rdata = raw[0], raw[1:]
            value = value + rdata
            if rtype == "0":
                break

        values.append(int(value, 2))
        packet = Packet(version, packet_type, values)
        packets.append(packet)

    else:
        length_type, bits = bits[0], bits[1:]
        if length_type == "1":
            length, bits = int(bits[:11], 2), bits[11:]

            while length > 0:
                subpackets, bits = read(bits)
                values.extend(subpackets)
                length = length - 1

            packets.append(Packet(version, packet_type, values))

        else:
            length, bits = int(bits[:15], 2), bits[15:]

            vbits, bits = bits[:length], bits[length:]
            while len(vbits) > 0:
                subpackets, vbits = read(vbits)
                values.extend(subpackets)

            packets.append(Packet(version, packet_type, values))

    return packets, bits

def version_sum(packet):
    count = 0
    count = count + packet.version
    for value in packet.values:
        if isinstance(value, Packet):
            count = count + version_sum(value)

    return count

def product(xs):
    result = 1
    for x in xs:
        result = result * x

    return result

def resolve(packet):
    ops = dict()
    ops[0] = sum
    ops[1] = product
    ops[2] = min
    ops[3] = max
    ops[4] = lambda xs: xs[0]
    ops[5] = lambda pair: 1 if pair[0] > pair[1] else 0
    ops[6] = lambda pair: 1 if pair[0] < pair[1] else 0
    ops[7] = lambda pair: 1 if pair[0] == pair[1] else 0

    values = list()
    for pv in packet.values:
        value = pv if isinstance(pv, int) else resolve(pv)
        values.append(value)

    op = ops[packet.type]
    result = op(values)
    return result

def d16p1(puzzle_input):
    bits = parse(puzzle_input)
    packets, bits = read(bits)
    return version_sum(packets[0])

def d16p2(puzzle_input):
    bits = parse(puzzle_input)
    packets, bits = read(bits)
    return resolve(packets[0])

def solve(puzzle_input):
    return d16p1(puzzle_input), d16p2(puzzle_input)

