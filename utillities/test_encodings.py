# student meter voltage encoding
from pymodbus.excepions import ModbusIOException 
import struct 
def convert_MSW_and_LSW_into_float(client ,address,  id):
    if not ModbusIOException:
   	    readings = client.read_holding_registers(address, 2, id)
   	    MSW_and_LSW_combined = readings.registers[0] << 16 | readings.registers[1]
   	    result = struct.unpack('>f', struct.pack('>I', MSW_and_LSW_combined))[0]
   	    return result
    else:
        return ModbusIOException

def student_voltage_conversion_into_float(client, address, id):
    #this needs debugging 
    if not ModbusIOException:
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
    else:
        return ModbusIOException


    
def student_current_conversion_into_float(client, address, id):

    if not ModbusIOException:
        readings = client.read_holding_registers(address, 1, id)
        address = radings.registers[0]
        s = address & 0x8000 # check sign 
        m = address & 0x4000 # check if mV or V, m stands for milli
        f = (address & 0x3FFF)/100
        if(s == 1):
            f = f* -1
        if(m == 1):
            f = f/1000
        return f
    else: 
        return ModbusIOException


