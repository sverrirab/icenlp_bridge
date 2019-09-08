#!/usr/bin/env python3

import argparse
import asyncio
import struct

from typing import Any, NoReturn

_PACKET_SIZE = 512
_DATA_SIZE = 504   # 512 - 2 * 4


def writeHeader(writer: Any, num_packets: int) -> NoReturn:
    writer.write(struct.pack('!i', 1))
    writer.write(struct.pack('!i', num_packets))
    writer.write(struct.pack('b', 0) * (_PACKET_SIZE - 2*4))


def writeData(writer: Any, data: bytes) -> NoReturn:
    writer.write(struct.pack('!ii', 2, len(data)))
    writer.write(data)
    if len(data) < _DATA_SIZE:
        writer.write(struct.pack('b', 0) * (_DATA_SIZE - len(data)))


async def icenlp_client(message: str) -> str:
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 1234)

    encoded = message.encode('utf-8')
    out_packets = (len(encoded) // _DATA_SIZE) + 1
    writeHeader(writer, out_packets)
    for i in range(out_packets):
        offset = _DATA_SIZE * i
        writeData(writer, encoded[offset:offset + _DATA_SIZE])

    data = await reader.readexactly(_PACKET_SIZE)
    opcode, num_packets = struct.unpack('!ii', data[0:8])
    assert opcode == 3, "Invalid opcode received"

    received_data = []

    for i in range(num_packets):
        data = await reader.readexactly(_PACKET_SIZE)
        opcode, len_data = struct.unpack('!ii', data[0:8])
        assert opcode == 4, "Invalid opcode received"
        received_data.append(data[8:len_data + 8])

    received = b''.join(received_data)

    writer.close()
    await writer.wait_closed()

    return received.decode('utf-8')


def parse(text: str) -> str:
    asyncio.run(icenlp_client(text))


def main():
    parser = argparse.ArgumentParser(
        description='Bridge for IceNLP')

    parser.add_argument(
        '-v', '--verbose', action='count', default=0,
        help='Increase output verbosity')
    parser.add_argument('filename', help='File to read and parse')

    args = parser.parse_args()

    with open(args.filename) as input:
        process = input.read()
        for line in process.split('\n'):
            print(process)

            parse(process)


if __name__ == '__main__':
    main()