from TLVProtocol import TLVData, DataTypes, decode, encode

json = TLVData(DataTypes.JSON, {"name":"Ahmad", "age": 19})
bson = TLVData(DataTypes.BSON, {"name":"Ahmad", "age": 19})
string = TLVData(DataTypes.STRING, '{"name": "Ahmad", "age": 19}')



def tests(name, func, testlist:list[dict]):
    overall_res = f'{name} tests Start\n\n'
    num_ok = 0
    for index, test in enumerate(testlist):
        overall_res += f"{name}_test {index}\n"
        res = func(**test["inputs"])
        overall_res += f"res > {res} = {test['outputs']} < out\n" 
        if res== test["outputs"]:
            overall_res += "OK\n"
            num_ok += 1
            continue
        overall_res += "failed\n"
    overall_res += f'\n\n passed: {num_ok}, failed: {len(testlist)-num_ok}'
    return overall_res

encode_datas = [
    {"inputs":{"tlvdata": json}, "outputs": b'{"name": "Ahmad", "age": 19}'},
    {"inputs":{"tlvdata": string}, "outputs": b'{"name": "Ahmad", "age": 19}'},
    {"inputs":{"tlvdata": bson}, "outputs": b'\x1e\x00\x00\x00\x02name\x00\x06\x00\x00\x00Ahmad\x00\x10age\x00\x13\x00\x00\x00\x00'}
]

print(tests("encode", encode, encode_datas))
json_encoded = b'{"name": "Ahmad", "age": 19}'
string_encoded = b'{"name": "Ahmad", "age": 19}'
bson_encoded = b'\x1e\x00\x00\x00\x02name\x00\x06\x00\x00\x00Ahmad\x00\x10age\x00\x13\x00\x00\x00\x00'

decode_datas = [
    {"inputs":{"byte": json_encoded, "datatype": DataTypes.JSON}, "outputs": json},
    {"inputs":{"byte": string_encoded, "datatype": DataTypes.STRING}, "outputs": string},
    {"inputs":{"byte": bson_encoded, "datatype": DataTypes.BSON}, "outputs": bson}
]

print(tests("decode", decode, decode_datas))