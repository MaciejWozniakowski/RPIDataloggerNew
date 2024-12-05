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


#combines MSW and LSW into real desired float value of 
#values gathered from the student meter each require different encoding
#hence the functions below

#def student_voltage_conversion_into_float(client, address, id):
#   #this needs debugging

#   readings = client.read_holding_registers(address,2 , id)
#   address1 = readings.registers[0]
#   print("r1",readings.registers[0],"e2", readings.registers[1])
#   address2 = readings.registers[1]
#   r = address1 & 0x3FF 
#   s = address1 & 0x8000
#   m = address1 & 0x4000
#   d = address2
#   if(d>0):
#       f = r + d/100
#   else:
#       f = r
#   if(m == 0):
#       f = f 
#   else:
#       f = f/1000
#       #    f = r + d/100 if d>0 else r
#    f = f if m == 0 else f/1000
#   return f if s == 0 else f*-1

def student_voltage_conversion_into_float(client, address, id):
#   #this needs debugging

    readings = client.read_holding_registers(address,2 , id)
    register1 = readings.registers[0]
    register2 = readings.registers[1]
    sign_bit = (register1 >> 15) & 1  # Bit 15: sign
    unit_bit = (register1 >> 14) & 1  # Bit 14: unit indicator
    integer_part = (register1 >> 4) & 0x3FF  # Bits 4–13: integer part (10 bits)
    
    # Decode fractional part from the second register
    fractional_part = (register2 >> 1) & 0x7F  # Bits 1–7: fractional part (7 bits)

    # Calculate the final value
    sign = -1 if sign_bit else 1
    value = sign * (integer_part + fractional_part / 128.0)

    # Apply unit scaling if the unit bit is set
    #if unit_bit:
    #    value *= 10

    return value

def student_current_conversion_into_float(client, address, id):
    readings = client.read_holding_registers(address, 1, id)
    bin_value = readings.registers[0]

    s = bin_value & 0x8000 # check sign 
    m = bin_value & 0x4000 # check if mV or V, m stands for milli
    f = (bin_value & 0x3FFF)/100
    if(s == 1):
        f = f* -1
    if(m == 1):
        f = f/1000
    return f

def student_active_power_conversion_into_float(client, address, id):
    readings = client.read_holding_registers(address, 1, id)
    binary_value = readings[0]
    s = binary_value & 0x8000 #check sign
    f = (binary_value & 0x3FFF)/10 # floating point value
    if(s == 1):
        f = f * -1
    return f

def run_and_read_client_9600():
    default_gateway_ip = '10.0.10.51'

    server_port = 502

    client = ModbusTcpClient(default_gateway_ip, port = server_port, 
                             #framer = framer
                             )

    #start the client
    client.connect()
    #test if the client has been connnected 
    assert client.connected 
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





    try:

        # first student meter has id of 3 and baudrate 9600, only holding registers 1-18 are accesible
        student_meter_voltage1 =  student_voltage_conversion_into_float(client,student_voltage_RMS_address1, 3 )
        student_meter_voltage2 = student_voltage_conversion_into_float(client,student_voltage_RMS_address2, 3) 
        print(student_meter_voltage1, student_meter_voltage2)
        student_meter_current1 = student_current_conversion_into_float(client, student_current_RMS_address1, 3) 
        #student_meter_current2 = student_current_conversion_into_float(client, student_current_RMS_address2, 3) 
        print(student_meter_current1)
        student_meter_active_power_1 = student_active_power_conversion_into_float(client, student_active_power_address1, 3) 
        student_meter_active_power_2 = student_active_power_conversion_into_float(client, student_active_power_address2, 3) 
        print(student_meter_active_power_1, student_meter_active_power_2)

        
        #student_meter_1_entry = ("DCmeter_3_1", student_meter_voltage1,student_meter_current1, student_meter_active_power_1)

        #student_meter_2_entry = ("DCmeter_3_2",student_meter_voltage2,student_meter_current2, student_meter_active_power_2)
        #print(student_meter_1_entry)
        #print(student_meter_2_entry)
        #return(student_meter_1_entry, student_meter_2_entry)
        
        

            
    except ModbusException as exc:
        print(f"Recieved exception {exc}")
        client.close()
        
                

run_and_read_client_9600()


