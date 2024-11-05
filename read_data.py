#from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusIOException
from pymodbus.client import ModbusTcpClient
#from pymodbus.transaction import ModbusSocketFramer  
from pymodbus import (
    ExceptionResponse,
    ModbusException,
    pymodbus_apply_logging_config,
) 
import time 

        
def run_async_simple_client():
    default_gateway_ip = '10.0.10.9'
    server_port = 502
    start_address = 102

    client = ModbusTcpClient(default_gateway_ip,port = server_port)

    #start the client
    print("trying to connect to the server")
    client.connect()
    #test if the client has been connnected 
    assert client.connected 

    voltage_RMS_address = 0
    current_RMS_address = 0 
    active_power_address = 0 
    total_energy_address = 0 
    status_address = 0
    try:
#       read every measurement necessary
#       DC meters 
#       For DC meters read only the Voltage RMS, Current RMS, Active Power, Total energy measurement, Status
        meter89 = client.read_holding_registers(start_address, 10 , 89) 
        print("Reading meter 89", meter89.registers)

        meter21 = client.read_holding_registers(start_address, 10 ,21) 
        print("Reading meter 21", meter21.registers)

        meter83 = client.read_holding_registers(start_address, 10 ,83) 
        print("Reading meter 21", meter83.registers)

        meter57 = client.read_holding_registers(start_address, 10 ,57) 
        print("Reading meter 57", meter57.registers)

        meter26 = client.read_holding_registers(start_address, 10 ,26) 
        print("Reading meter 26", meter26.registers)
        print("All DC meters are done")
#       AC meters 

#        result  = client.read_holding_registers(start_address, 10 ,unit_id)#i have no idea what will be red 
        

            
        print("past client read holding registers")
        time.sleep(1)
    except ModbusException as exc:
        print(f"Recieved exception {exc}")
        client.close()
        return

run_async_simple_client()




