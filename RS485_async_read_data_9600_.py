#from pymodbus.client import ModbusSerialClient
import struct 
from pymodbus.exceptions import ModbusIOException
#from pymodbus.client import AsyncModbusTcpClient as ModbusTcpClient
from pymodbus.client import AsyncModbusSerialClient
import asyncio
#from pymodbus.transaction import ModbusSocketFramer  
from pymodbus import (
    ExceptionResponse,
    #FramerType,
    ModbusException,
    pymodbus_apply_logging_config,
) 



async def student_voltage_conversion_into_float(client, address, id):
    #this needs debugging
    try:
        readings = await client.read_holding_registers(address, 2, id)
        address1 = readings.registers[0]
        address2 = readings.registers[1]
        r = address1 & 0x3FF 
        s = address1 & 0x8000
        m = address1 & 0x4000
        d = address2 & 0x7F 

        f = r + d / 100 if d > 0 else r  # Adds `d` divided by 100 to `r`, unless `d` is 0.
        f = f if m == 0 else f / 1000  # Scales `f` down by 1000 if the 15th bit (`m`) is set.
    
        return f if s == 0 else f * -1  # Negates `f` if the 16th bit (`s`) is set (sign).
    except asyncio.CancelledError:
        print("Cancelled")
    except:
        return None
    
async def student_current_conversion_into_float(client, address, id):
    try:
        readings = await client.read_holding_registers(address, 1, id)
        bin_value = readings.registers[0]

        s = bin_value & 0x8000 # check sign 
        m = bin_value & 0x4000 # check if mV or V, m stands for milli
        f = (bin_value & 0x3FFF)/100
        if(s == 1):
            f = f* -1
        if(m != 0):
            f = f/1000
        return f
    except asyncio.CancelledError:
        print("Cancelled")
    except:
        return None

async def student_active_power_conversion_into_float(client, address, id):
    try:    
        readings = await client.read_holding_registers(address, 1, id)
        binary_value = readings.registers[0]
        s = binary_value & 0x8000 #check sign
        f = (binary_value & 0x3FFF)/10 # floating point value
        if(s == 1):
            f = f * -1
        return f
    except asyncio.CancelledError:
        print("Cancelled")
    except: 
        return None
async def run_and_read_client_9600():
    #    port = "/dev/ttyAMA3"
    port = "/dev/ttyAMA5"

    baudrate = 9600 
    parity = 'N'
    stopbits = 1

    client = AsyncModbusSerialClient( port = port,baudrate=baudrate, parity = parity, stopbits = stopbits
                             #framer = framer
                             )

    await client.connect()
    assert client.connected 

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
        ###
        ### METER ID 2 
        ###
        student_meter_voltage_2_1 = await student_voltage_conversion_into_float(client,student_voltage_RMS_address1, 2 )
        student_meter_active_power_2_1 = await student_active_power_conversion_into_float(client, student_active_power_address1, 2) 
        student_meter_current_2_1 = await student_current_conversion_into_float(client, student_current_RMS_address1, 2) 
        student_meter_voltage_2_2 = await student_voltage_conversion_into_float(client,student_voltage_RMS_address2, 2)
        student_meter_current_2_2 = await student_current_conversion_into_float(client, student_current_RMS_address2, 2) 
        student_meter_active_power_2_2 = await student_active_power_conversion_into_float(client, student_active_power_address2, 2) 

        
        student_meter_2_1_entry = ("DCmeter_2_1",student_meter_voltage_2_1, student_meter_current_2_1, student_meter_active_power_2_1)
        student_meter_2_2_entry = ("DCmeter_2_2",student_meter_voltage_2_2, student_meter_current_2_2, student_meter_active_power_2_2)
        #print(student_meter_2_1_entry)
        #print(student_meter_2_2_entry)
        # 
        #METER ID 3
        #

        student_meter_voltage_3_1 = await student_voltage_conversion_into_float(client,student_voltage_RMS_address1, 3 )
        student_meter_active_power_3_1 = await student_active_power_conversion_into_float(client, student_active_power_address1, 3) 
        student_meter_current_3_1 = await student_current_conversion_into_float(client, student_current_RMS_address1, 3) 
        student_meter_voltage_3_2 = await student_voltage_conversion_into_float(client,student_voltage_RMS_address2, 3)
        student_meter_current_3_2 = await student_current_conversion_into_float(client, student_current_RMS_address2, 3) 
        student_meter_active_power_3_2 = await student_active_power_conversion_into_float(client, student_active_power_address2, 3) 

        
        student_meter_3_1_entry = ("DCmeter_3_1",student_meter_voltage_3_1, student_meter_current_3_1, student_meter_active_power_3_1)
        student_meter_3_2_entry = ("DCmeter_3_2",student_meter_voltage_3_2, student_meter_current_3_2, student_meter_active_power_3_2)
        #print(student_meter_3_1_entry)
        #print(student_meter_3_2_entry)
        # 
        #METER ID 4
        #

        student_meter_voltage_4_1 = await student_voltage_conversion_into_float(client,student_voltage_RMS_address1, 4 )
        student_meter_active_power_4_1 = await student_active_power_conversion_into_float(client, student_active_power_address1, 4) 
        student_meter_current_4_1 = await student_current_conversion_into_float(client, student_current_RMS_address1, 4) 
        student_meter_voltage_4_2 = await student_voltage_conversion_into_float(client,student_voltage_RMS_address2, 4)
        student_meter_current_4_2 = await student_current_conversion_into_float(client, student_current_RMS_address2, 4) 
        student_meter_active_power_4_2 = await student_active_power_conversion_into_float(client, student_active_power_address2, 4) 

        
        student_meter_4_1_entry = ("DCmeter_4_1",student_meter_voltage_4_1, student_meter_current_4_1, student_meter_active_power_4_1)
        student_meter_4_2_entry = ("DCmeter_4_2",student_meter_voltage_4_2, student_meter_current_4_2, student_meter_active_power_4_2)
        #print(student_meter_4_1_entry)
        #print(student_meter_4_2_entry)
        return(student_meter_2_1_entry, student_meter_2_2_entry ,student_meter_3_1_entry, student_meter_3_2_entry, student_meter_4_1_entry, student_meter_4_2_entry)
    except asyncio.CancelledError:
        print("Cancelled")
        
        

            
    except ModbusException as exc:
        print(f"Recieved exception {exc}")
        client.close()
        
                

asyncio.run(run_and_read_client_9600())


