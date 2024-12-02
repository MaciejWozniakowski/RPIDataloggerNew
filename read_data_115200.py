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

    AC_voltage_phase_1neutral_address = 1 
    AC_voltage_phase_2neutral_address =3 
    AC_voltage_phase_3neutral_address = 5 
    AC_current_phase_1_address = 13
    AC_current_phase_2_address = 15
    AC_current_phase_3_address = 17
    AC_phase_1_power_address = 19
    AC_phase_2_power_address = 21
    AC_phase_3_power_address = 23
    AC_frequency_grid_address = 52
    AC_P_total_address = 41 
    AC_Q_total_address = 45
    AC_S_total_address = 43





    try:
#       read every measurement necessary
#       DC meters 
#       For DC meters read only the Voltage RMS, Current RMS, Active Power, Total energy measurement, Status

        meter89_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 89)
        meter89_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 89)
        meter89_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 89)
        meter_89_entry = ("DCmeter_89",meter89_voltage, meter89_current,meter89_power)
        print(f"Reading meter 89, voltage {meter89_voltage}, current {meter89_current}, power {meter89_power}")

        meter21_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 21)
        meter21_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 21)
        meter21_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 21)
        meter_21_entry = ("DCmeter_21",meter21_voltage, meter21_current,meter21_power)
        print(f"Reading meter 21, voltage {meter21_voltage}, current {meter21_current}, power {meter21_power}")
        #rr = client.read_holding_registers(104, 2, 21)
        #print("meter21 = ", rr.registers)
        
        meter83_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 83)
        meter83_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 83)
        meter83_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 83)
        meter_83_entry = ("DCmeter_83",meter83_voltage, meter83_current,meter83_power)
        print(f"Reading meter 83, voltage {meter83_voltage}, current {meter83_current}, power {meter83_power}")


        meter57_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 57)
        meter57_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 57)
        meter57_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 57)
        meter_57_entry = ("DCmeter_57",meter57_voltage, meter57_current,meter57_power)
        print(f"Reading meter 57, voltage {meter57_voltage}, current {meter57_current}, power {meter57_power}")
        #meter57 = client.read_holding_registers(start_address, 10 ,57) 

        meter26_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 26)
        meter26_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 26)
        meter26_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 26)
        meter_26_entry = ("DCmeter_26",meter26_voltage, meter26_current,meter26_power)
        print(f"Reading meter 26, voltage {meter26_voltage}, current {meter26_current}, power {meter26_power}")
        #        meter26 = client.read_holding_registers(start_address, 10 ,26) 

        
        print("All DC meters are done")
        #the new AC meter 
        meter_AC_test = client.read_holding_registers(1, 8, 1)
        AC_voltage_phase_1neutral = convert_MSW_and_LSW_into_float(client, AC_voltage_phase_1neutral_address,1)   
        AC_voltage_phase_2neutral = convert_MSW_and_LSW_into_float(client, AC_voltage_phase_2neutral_address,1)   
        AC_voltage_phase_3neutral = convert_MSW_and_LSW_into_float(client, AC_voltage_phase_3neutral_address,1)   
        AC_current_1 = convert_MSW_and_LSW_into_float(client, AC_current_phase_1_address,1)   
        AC_current_2 = convert_MSW_and_LSW_into_float(client, AC_current_phase_2_address,1)   
        AC_current_3 = convert_MSW_and_LSW_into_float(client, AC_current_phase_3_address,1)   
        AC_phase_1_power = convert_MSW_and_LSW_into_float(client, AC_phase_1_power_address, 1)
        AC_phase_2_power = convert_MSW_and_LSW_into_float(client, AC_phase_2_power_address, 1)
        AC_phase_3_power = convert_MSW_and_LSW_into_float(client, AC_phase_3_power_address, 1)
        AC_frequency_grid = #this is only one word convert_MSW_and_LSW_into_float(client, AC_frequency_grid_address, 1)
        AC_P_total = convert_MSW_and_LSW_into_float(client, AC_P_total_address, 1)
        AC_Q_total = convert_MSW_and_LSW_into_float(client, AC_Q_total_address, 1)
        AC_S_total = convert_MSW_and_LSW_into_float(client, AC_S_total_address, 1)
        AC_meter_entry = ("ACmeter", AC_voltage_phase_1neutral, AC_voltage_phase_2neutral, AC_voltage_phase_3neutral, AC_current_1, AC_current_2, AC_current_3, AC_phase_1_power,  AC_phase_2_power, AC_phase_3_power, AC_frequency_grid, AC_P_total, AC_Q_total, AC_S_total)

        return (meter_89_entry, meter_21_entry , meter_83_entry, meter_57_entry, meter_26_entry, AC_meter_entry) 
        
        

            
    except ModbusException as exc:
        print(f"Recieved exception {exc}")
        client.close()
        return





