from pymodbus.exceptions import ModbusIOException
from pymodbus.client import ModbusTcpClient
#from pymodbus.transaction import ModbusSocketFramer  
from pymodbus import (
    ExceptionResponse,
    ModbusException,
    pymodbus_apply_logging_config,
) 

# Configure client (example for an RS-485 connection)
client = ModbusTcpClient('10.0.10.9', port = 502)

if client.connect():

    for device_id in range(0, 256):  # Scan IDs from 1 to 255
        print(device_id)
        response = client.read_holding_registers(0, 1 ,device_id)
        if not isinstance(response, ModbusIOException):
            print(f"Found Modbus Slave ID: {device_id}")

        
    client.close()
else:
    print("Failed to connect to Modbus network.")
