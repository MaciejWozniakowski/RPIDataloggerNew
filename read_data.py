#from pymodbus.client import ModbusSerialClient
import struct 
from pymodbus.exceptions import ModbusIOException
from pymodbus.client import ModbusTcpClient
#from pymodbus.transaction import ModbusSocketFramer  
from pymodbus import (
    ExceptionResponse,
    ModbusException,
    pymodbus_apply_logging_config,
) 
import time 
#combines MSW and LSW into real desired float value of 
def convert_MSW_and_LSW_into_float(client ,address,  id):
    readings = client.read_holding_registers(address, 2, id)
    MSW_and_LSW_combined = readings.registers[0] << 16 | readings.registers[1]
    result = struct.unpack('>f', struct.pack('>I', MSW_and_LSW_combined))[0]
    return result

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

    voltage_RMS_address = 104 # 139-142
    current_RMS_address = 106 # 143 - 146 
    active_power_address = 108 #147 - 150
    try:
#       read every measurement necessary
#       DC meters 
#       For DC meters read only the Voltage RMS, Current RMS, Active Power, Total energy measurement, Status

#        meter89 = client.read_holding_registers(voltage_RMS_address, 10 , 89) 
        meter89_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 89)
        meter89_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 89)
        meter89_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 89)
        print(f"Reading meter 89, voltage {meter89_voltage}, current {meter89_current}, power {meter89_power}")

        meter21_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 21)
        meter21_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 21)
        meter21_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 21)
        print(f"Reading meter 21, voltage {meter21_voltage}, current {meter21_current}, power {meter21_power}")
        
        meter83_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 83)
        meter83_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 83)
        meter83_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 83)
        print(f"Reading meter 83, voltage {meter83_voltage}, current {meter83_current}, power {meter83_power}")


        meter57_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 57)
        meter57_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 57)
        meter57_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 57)
        print(f"Reading meter 57, voltage {meter57_voltage}, current {meter57_current}, power {meter57_power}")
        #meter57 = client.read_holding_registers(start_address, 10 ,57) 

        meter26_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 26)
        meter26_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 26)
        meter26_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 26)
        print(f"Reading meter 26, voltage {meter26_voltage}, current {meter26_current}, power {meter26_power}")
        #        meter26 = client.read_holding_registers(start_address, 10 ,26) 
        print("All DC meters are done")
#       AC meters 
        
        

            
        print("past client read holding registers")
        time.sleep(1)
    except ModbusException as exc:
        print(f"Recieved exception {exc}")
        client.close()
        return

run_async_simple_client()




