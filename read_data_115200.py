import struct 
from pymodbus.exceptions import ModbusIOException
from pymodbus.client import ModbusTcpClient
#from pymodbus.transaction import ModbusSocketFramer  
from pymodbus import (
    ExceptionResponse,
    FramerType,
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
def convert_carlo_gavazzi(client, address, id):
    readings = client.read_holding_registers( address,2, id)
    lsw = readings.registers[1] & 0xFFFF  # Mask to 16 bits
    msw = readings.registers[0] & 0xFFFF  # Mask to 16 bits

    # Combine LSW and MSW in the order LSW -> MSW
    combined = (msw << 16) | lsw

    # Convert to signed INT32 if necessary
    if combined >= 0x80000000:
        combined -= 0x100000000

    return combined/10

def run_and_read_client_115200():
    #default_gateway_ip = '10.0.10.51'

    default_gateway_ip = '10.0.10.52'

    server_port = 502
    framer = FramerType.SOCKET

    client = ModbusTcpClient(default_gateway_ip, port = server_port, 
                             framer = framer
                             )

    client.connect()
    assert client.connected 
    #non student made DC meters 
    voltage_RMS_address = 104 # 139-142
    current_RMS_address = 106 # 143 - 146 
    active_power_address = 108 #147 - 150

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

        #print("meter 89 ",client.read_holding_registers(voltage_RMS_address, 2, 89))

        meter89_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 89)
        meter89_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 89)
        meter89_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 89)
        meter_89_entry = ("DCmeter_89",meter89_voltage, meter89_current,meter89_power)
        #print(f"Reading meter 89, voltage {meter89_voltage}, current {meter89_current}, power {meter89_power}")

        #print("meter 21",client.read_holding_registers(voltage_RMS_address, 2, 21))

        meter21_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 21)
        meter21_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 21)
        meter21_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 21)
        meter_21_entry = ("DCmeter_21",meter21_voltage, meter21_current,meter21_power)
        #print(f"Reading meter 21, voltage {meter21_voltage}, current {meter21_current}, power {meter21_power}")
        
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


        meter26_voltage = convert_MSW_and_LSW_into_float(client, voltage_RMS_address, 26)
        meter26_current = convert_MSW_and_LSW_into_float(client, current_RMS_address, 26)
        meter26_power =  convert_MSW_and_LSW_into_float(client, active_power_address, 26)
        meter_26_entry = ("DCmeter_26",meter26_voltage, meter26_current,meter26_power)
        print(f"Reading meter 26, voltage {meter26_voltage}, current {meter26_current}, power {meter26_power}")
        
        print("Debug encoding carlo gavazzi:", convert_carlo_gavazzi(client, AC_voltage_phase_1neutral_address, 2))
        
        #the new AC meter 
#        meter_AC_test = client.read_holding_registers(333, 2, 2)
#        print("AC ", meter_AC_test)
        #print("AC ",meter_AC_test)
        AC_voltage_phase_1neutral = convert_MSW_and_LSW_into_float(client, AC_voltage_phase_1neutral_address,2)   
        AC_voltage_phase_2neutral = convert_MSW_and_LSW_into_float(client, AC_voltage_phase_2neutral_address,2)   
        AC_voltage_phase_3neutral = convert_MSW_and_LSW_into_float(client, AC_voltage_phase_3neutral_address,2)   
        AC_current_1 = convert_MSW_and_LSW_into_float(client, AC_current_phase_1_address,2)   
        AC_current_2 = convert_MSW_and_LSW_into_float(client, AC_current_phase_2_address,2)   
        AC_current_3 = convert_MSW_and_LSW_into_float(client, AC_current_phase_3_address,2)   
        AC_phase_1_power = convert_MSW_and_LSW_into_float(client, AC_phase_1_power_address, 2)
        AC_phase_2_power = convert_MSW_and_LSW_into_float(client, AC_phase_2_power_address, 2)
        AC_phase_3_power = convert_MSW_and_LSW_into_float(client, AC_phase_3_power_address, 2)
        AC_frequency_grid = client.read_holding_registers(AC_frequency_grid_address, 1, 2)  #this is only one word convert_MSW_and_LSW_into_float(client, AC_frequency_grid_address, 1)
        AC_P_total = convert_MSW_and_LSW_into_float(client, AC_P_total_address, 2)
        AC_Q_total = convert_MSW_and_LSW_into_float(client, AC_Q_total_address, 2)
        AC_S_total = convert_MSW_and_LSW_into_float(client, AC_S_total_address, 2)
        AC_meter_entry = ("ACmeter", AC_voltage_phase_1neutral, AC_voltage_phase_2neutral, AC_voltage_phase_3neutral, AC_current_1, AC_current_2, AC_current_3, AC_phase_1_power,  AC_phase_2_power, AC_phase_3_power,  AC_P_total, AC_Q_total, AC_S_total)
        #print(AC_meter_entry)
        #return (meter_89_entry, meter_21_entry , meter_83_entry, meter_57_entry, meter_26_entry, AC_meter_entry) 
        return (meter_89_entry, meter_21_entry , meter_83_entry, meter_57_entry, meter_26_entry ) 
        
        

            
    except ModbusException as exc:
        print(f"Recieved exception {exc}")
        client.close()
        return



run_and_read_client_115200()
