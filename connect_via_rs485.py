from pymodbus.exceptions import ModbusIOException
from pymodbus.client import ModbusSerialClient
from pymodbus.framer import FramerType.RTU 
        
port1 = "/dev/ttyAMA3"
port2 = "/dev/ttyAMA5"
framer=FramerType.RTU


client = ModbusSerialClient(port2, baudrate=9600, bytesize=8, parity="N", stopbits=1)
client.connect()
assert client.connect

if client.connect():
    rr = client.read_holding_registers(30001, 2, 1)
    print(rr)

        
    client.close()
