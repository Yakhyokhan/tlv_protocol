import enum, json, bson, socket

class DataTypes(enum.IntEnum):
    JSON = 1
    BSON = 2
    STRING = 3

def encode(tlvdata): 
    datatype = tlvdata.type
    data = tlvdata.data
    if  datatype == DataTypes.JSON:
        json_format = json.dumps(data)
        return json_format.encode()
    if datatype == DataTypes.BSON:
        return bson.dumps(data)
    if datatype == DataTypes.STRING:
        return str.encode(data)

def decode(byte: bytes, datatype, length = -1):
    if  datatype == DataTypes.JSON:
        json_format = byte.decode()
        data = json.loads(json_format)
        return TLVData(datatype, data, length)
    if datatype == DataTypes.BSON:
        data =  bson.loads(byte)
        return TLVData(datatype, data, length)
    if datatype == DataTypes.STRING:
        data =  byte.decode()
        return TLVData(datatype, data, length)

class TLVData(object):
    def __init__(self, type, data, length = -1) -> None:
        self.type: int = type
        self.length: int = length
        self.data = data

    def __repr__(self) -> str:
        return f"TLVData(type:{self.type}, len: {self.length}, data:{self.data})"
    
    def __eq__(self, __value: object) -> bool:
        return self.type == __value.type and self.data == __value.data

    def encode(self):
        return encode(self)
    
    @classmethod
    def decode(cls, byte, datatype, length):
        return decode(byte, datatype, length)
    
def read(conn: socket.socket):
    buf = conn.recv(3)
    type = buf[0]
    length = int.from_bytes(buf[1:])
    databyte = conn.recv(length)
    data = decode(databyte, type, length)
    return data

def write(conn: socket.socket, tlvdata: TLVData):
    databyte = tlvdata.encode()
    if tlvdata.length == -1:
        tlvdata.length = len(databyte)
    type_length = tlvdata.type.to_bytes() + tlvdata.length.to_bytes(2)
    conn.send(type_length)
    conn.send(databyte)


