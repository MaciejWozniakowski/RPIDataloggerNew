# student meter voltage encoding
import struct 
def convert_MSW_and_LSW_into_float(client ,address,  id):
    readings = client.read_holding_registers(address, 2, id)
    MSW_and_LSW_combined = readings.registers[0] << 16 | readings.registers[1]
    result = struct.unpack('>f', struct.pack('>I', MSW_and_LSW_combined))[0]
    return result

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
    f = (address & 0x3FFF)/100 #floating point value
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


def my_student_voltage_conversion(word1, word2):
    print("bin word 1", bin(word1), "bin word 2", bin(word2))
    r = word1 & 0x3FF 
    s = word1 & 0x8000
    m = word1 & 0x4000
    d = word2 & 0x7F 

    f = r + d / 100 if d > 0 else r  # Adds `d` divided by 100 to `r`, unless `d` is 0.
    f = f if m == 0 else f / 1000  # Scales `f` down by 1000 if the 15th bit (`m`) is set.
    
    return f if s == 0 else f * -1  # Negates `f` if the 16th bit (`s`) is set (sign).

print(my_student_voltage_conversion(0b11011100, 0b100000))
