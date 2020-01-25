import asyncio
import struct

from typing import Any, Optional

_PACKET_SIZE = 512
_DATA_SIZE = 504   # 512 - 2 * 4

_hostname = 'localhost'
_port = 1234


def writeHeader(writer: Any, num_packets: int) -> None:
    writer.write(struct.pack('!i', 1))
    writer.write(struct.pack('!i', num_packets))
    writer.write(struct.pack('b', 0) * (_PACKET_SIZE - 2*4))


def writeData(writer: Any, data: bytes) -> None:
    writer.write(struct.pack('!ii', 2, len(data)))
    writer.write(data)
    if len(data) < _DATA_SIZE:
        writer.write(struct.pack('b', 0) * (_DATA_SIZE - len(data)))


async def icenlp_client(message: str) -> str:
    reader, writer = await asyncio.open_connection(_hostname, _port)

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


def init(hostname: Optional[str] = None,
         port: Optional[int] = None) -> None:
    """Initialize IceNLP connection"""
    global _hostname, _port
    if hostname is not None:
        _hostname = hostname
    if port is not None:
        _port = port
    parse('Núna!')


def parse(text: str) -> str:
    """Parse text with IceNLP"""
    retries = 5
    while True:
        try:
            return asyncio.get_event_loop().run_until_complete(icenlp_client(text))
        except asyncio.streams.IncompleteReadError:
            retries -= 1
            if retries == 0:
                raise
