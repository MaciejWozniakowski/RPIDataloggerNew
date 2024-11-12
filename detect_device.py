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
    print("Connected to Modbus network.")
    response21 = client.read_holding_registers(139,1, 3)
    print("Check if meter 21 makes sense" ,response21.registers())
    for device_id in range(1, 256):  # Scan IDs from 1 to 255
        response = client.read_holding_registers(104, 1 ,device_id)
        if response.isError():
            print(f"No response from device ID {device_id}")
        else:
            print(f"Device found with ID: {device_id}")
            # Optional: Retrieve more info from the device
    client.close()
else:
    print("Failed to connect to Modbus network.")
