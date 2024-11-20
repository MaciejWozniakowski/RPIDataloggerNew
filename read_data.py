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
    if not ModbusIOException:
   	    readings = client.read_holding_registers(address, 2, id)
   	    MSW_and_LSW_combined = readings.registers[0] << 16 | readings.registers[1]
   	    result = struct.unpack('>f', struct.pack('>I', MSW_and_LSW_combined))[0]
   	    return result
    else:
        return ModbusIOException
#values gathered from the student meter each require different encoding
#hence the functions below

def student_voltage_conversion_into_float_RMS(client, adress1, address2, id):
    pass

def student_current_conversion_into_float_RMS(client, adress1, address2, id):
    pass

def student_active_power_conversion_into_float(client, adress1, address2, id):
    pass

def run_async_simple_client():
    default_gateway_ip = '10.0.10.9'
    server_port = 502

    client = ModbusTcpClient(default_gateway_ip, port = server_port)

    #start the client
    client.connect()
    #test if the client has been connnected 
    assert client.connected 
    print("Client connected")
    #non student made DC meters 
    voltage_RMS_address = 104 # 139-142
    current_RMS_address = 106 # 143 - 146 
    active_power_address = 108 #147 - 150
    #student made DC meter

    student_voltage_RMS_address1 = 2 # also 3 
    student_current_RMS_address1 = 4  
    student_active_power_address1 = 8
    student_EnergyCH1_address1 = 15 #also 16
    student_QCH1_address1 = 11 # also 12 

    student_voltage_RMS_address2 = 5 #also 6 
    student_current_RMS_address2 = 7  
    student_active_power_address2 = 9  
    student_EnergyCH2_address2 = 17 #also 18
    student_QCH2_address2 = 13 # also 14 
    #AC meter:

    AC_voltage_phase_1neutral_address = 30001 
    AC_voltage_phase_2neutral_address =30003 
    AC_voltage_phase_3neutral_address = 30005 
    AC_current_phase_1_address = 30007
    AC_current_phase_2_address = 30009
    AC_current_phase_3_address = 30011
    #add other values to be stored 





    try:
#       read every measurement necessary
#       DC meters 
#       For DC meters read only the Voltage RMS, Current RMS, Active Power, Total energy measurement, Status

       # meter89 = client.read_holding_registers(voltage_RMS_address, 2 , 89) 
        #print(meter89)
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

        # first student meter has id of 3 and baudrate 9600, only holding registers 1-18 are accesible
        #student_meter_voltage1 = client.read_holding_registers(3, 2, 3)
        #print(student_meter_voltage1,"some garbage DC value, just for tests")
        
        print("All DC meters are done")
#       AC meters 
        #AC meter has baudrate 9600 and slave id 50 

        #meter50_voltage = client.read_holding_registers(6, 2, 50)
        #print(meter50_voltage,"some garbage AC value, just for tests")
        
        

            
        time.sleep(1)
    except ModbusException as exc:
        print(f"Recieved exception {exc}")
        client.close()
        return

run_async_simple_client()




