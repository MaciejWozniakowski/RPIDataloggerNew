#from pymodbus.client import ModbusSerialClient
import struct 
from pymodbus.exceptions import ModbusIOException
from pymodbus.client import ModbusTcpClient
#from pymodbus.transaction import ModbusSocketFramer  
from pymodbus import (
    ExceptionResponse,
    #FramerType,
    ModbusException,
    pymodbus_apply_logging_config,
) 
import time

## 57 zyje
## 26 zyje
## 83 zyje
## 21 zyje
## 89 zyje


#combines MSW and LSW into real desired float value of 
def convert_MSW_and_LSW_into_float(client ,address,  id):

    readings = client.read_holding_registers(address, 2, id)
    MSW_and_LSW_combined = readings.registers[0] << 16 | readings.registers[1]
    result = struct.unpack('>f', struct.pack('>I', MSW_and_LSW_combined))[0]
    return result
#values gathered from the student meter each require different encoding
#hence the functions below

def student_voltage_conversion_into_float(client, address, id):
    #this needs debugging

    readings = client.read_holding_registers(address,2 , id)
    address1 = readings.registers[0]
    address2 = readings.registers[2]
    r = address1 & 0x3FF
    s = address1 & 0x8000
    m = address1 & 0x4000
    d = address2
    f = r + d/100 if d>0 else r
    f = f if m == 0 else f/1000
    return f if s == 0 else f*-1

def student_current_conversion_into_float(client, address, id):
    readings = client.read_holding_registers(address, 1, id)
    address = readings.registers[0]

    s = address & 0x8000 # check sign 
    m = address & 0x4000 # check if mV or V, m stands for milli
    f = (address & 0x3FFF)/100
    if(s == 1):
        f = f* -1
    if(m == 1):
        f = f/1000
    return f

def student_active_power_conversion_into_float(client, address1, address2, id):
    pass

def run_and_read_client_115200():
    default_gateway_ip = '10.0.10.8'

    server_port = 502
    #framer = FramerType.SOCKET

    client = ModbusTcpClient(default_gateway_ip, port = server_port, 
                             #framer = framer
                             )

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

        #meter89_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 89)
        #meter89_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 89)
        #meter89_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 89)
        #print(f"Reading meter 89, voltage {meter89_voltage}, current {meter89_current}, power {meter89_power}")
        meter21_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 21)
        meter21_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 21)
        meter21_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 21)

        meter_21_entry = [meter21_voltage, meter21_current,meter21_power]

        #rr = client.read_holding_registers(104, 2, 21)
        #print("meter21 = ", rr.registers)
        print(f"Reading meter 21, voltage {meter21_voltage}, current {meter21_current}, power {meter21_power}")
        
        #meter83_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 83)
        #meter83_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 83)
        #meter83_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 83)
        #print(f"Reading meter 83, voltage {meter83_voltage}, current {meter83_current}, power {meter83_power}")


        #meter57_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 57)
        #meter57_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 57)
        #meter57_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 57)
        #print(f"Reading meter 57, voltage {meter57_voltage}, current {meter57_current}, power {meter57_power}")
        #meter57 = client.read_holding_registers(start_address, 10 ,57) 

        #meter26_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 26)
        #meter26_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 26)
        #meter26_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 26)
        #print(f"Reading meter 26, voltage {meter26_voltage}, current {meter26_current}, power {meter26_power}")
        #        meter26 = client.read_holding_registers(start_address, 10 ,26) 

        # first student meter has id of 3 and baudrate 9600, only holding registers 1-18 are accesible
        #student_meter_voltage1 = client.read_holding_registers(3, 2, 3)
        #print(student_meter_voltage1,"some garbage DC value, just for tests")
        
        print("All DC meters are done")
        return meter_21_entry
#       AC meters 
        #AC meter has baudrate 9600 and slave id 50 

        #meter50_voltage = client.read_holding_registers(6, 2, 50)
        #print(meter50_voltage,"some garbage AC value, just for tests")
        
        

            
        time.sleep(1)
    except ModbusException as exc:
        print(f"Recieved exception {exc}")
        client.close()
        return




