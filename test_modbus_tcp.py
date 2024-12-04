from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('10.0.10.50')   # Create client object
client.connect()                           # connect to device
result = client.read_holding_registers(106, 1, 26)  # get information from device
print(result.bits[0])                      # use information
client.close()      
