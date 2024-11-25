import struct 
from pymodbus.exceptions import ModbusIOException
import pymodbus.client as ModbusClient
#from pymodbus.transaction import ModbusSocketFramer  
from pymodbus import (
    ExceptionResponse,
    FramerType,
    ModbusException,
    pymodbus_apply_logging_config,
) 
import time 

framer = FramerType.SOCKET
port1 = "/dev/ttyAMA3" 
port2 = "/dev/ttyAMA5"
client = ModbusClient.ModbusSerialClient(
            port1,
            framer=framer,
            # timeout=10,
            # retries=3,
            baudrate=9600,
            bytesize=8,
            parity="N",
            stopbits=1,
            # handle_local_echo=False,
        )


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

def run_client9600():

    client.connect()
    assert client.connected
    try:
        ## AC meter 
        ac_reading = client.read_holding_registers(AC_current_phase_1_address, 2, 50)
        ## student meter 
        student_reading = client.read_holding_registers(student_voltage_RMS_address1, 2, 3)
        print('ac_reading:', ac_reading,"student_reading", student_reading)
    except ModbusException as exc:
        print("Recieved exception", exc)
