import mysql.connector as mariadb
import numpy as np
from Imports import *

mariadb_connection = None
create_cursor = None

def SqlConnection():
    global create_cursor, mariadb_connection
    
    mariadb_connection = mariadb.connect(user='hpi.python', password='hpi.python', database='fc_1_data_db', host='192.168.2.148', port=3306)
    # mariadb_connection = mariadb.connect(user='hpi.python', password='hpi.python', host='192.168.2.148', port=3306)

    create_cursor = mariadb_connection.cursor()

def CreateDatabase(databaseName):
    global create_cursor

    create_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {databaseName}")

def ShowDatabase():
    global create_cursor

    create_cursor.execute("SHOW DATABASES")

    for x in create_cursor:
        print(x)

def CreateTable1():
    global create_cursor

    create_cursor.execute("CREATE TABLE table_test1 (Name VARCHAR(64), Date VARCHAR(64), MODELCODE VARCHAR(64))")

def CreateTable2():
    global create_cursor

    create_cursor.execute("CREATE TABLE PROCESS1_DATA (Name VARCHAR(64), Date VARCHAR(64), MODELCODE VARCHAR(64))")

def CreateProcess1Table():
    global create_cursor

    create_cursor.execute("""
        CREATE TABLE IF NOT EXISTS process1_data(
            Process_1_DATA_No VARCHAR(64),
            Process_1_DateTime VARCHAR(64) PRIMARY KEY,
            Process_1_Model_Code VARCHAR(64),
            Process_1_S_N VARCHAR(64),
            Process_1_ID VARCHAR(64),
            Process_1_NAME VARCHAR(64),
            Process_1_Regular_Contractual VARCHAR(64),
            Process_1_Em2p VARCHAR(64),
            Process_1_Em2p_Lot_No VARCHAR(64),
            Process_1_Em3p VARCHAR(64),
            Process_1_Em3p_Lot_No VARCHAR(64),
            Process_1_Harness VARCHAR(64),
            Process_1_Harness_Lot_No VARCHAR(64),
            Process_1_Frame VARCHAR(64),
            Process_1_Frame_Lot_No VARCHAR(64),
            Process_1_Bushing VARCHAR(64),
            Process_1_Bushing_Lot_No VARCHAR(64),
            Process_1_ST VARCHAR(64),
            Process_1_Actual_Time VARCHAR(64),
            Process_1_NG_Cause VARCHAR(64),
            Process_1_Repaired_Action VARCHAR(64)
        )
        """)
    
def CreateProcess2Table():
    global create_cursor

    create_cursor.execute("""
        CREATE TABLE IF NOT EXISTS process2_data(
            Process_2_DATA_No VARCHAR(64),
            Process_2_DateTime VARCHAR(64) PRIMARY KEY,
            Process_2_Model_Code VARCHAR(64),
            Process_2_S_N VARCHAR(64),
            Process_2_ID VARCHAR(64),
            Process_2_NAME VARCHAR(64),
            Process_2_Regular_Contractual VARCHAR(64),
            Process_2_M4x40_Screw VARCHAR(64),
            Process_2_M4x40_Screw_Lot_No VARCHAR(64),
            Process_2_Rod_Blk VARCHAR(64),
            Process_2_Rod_Blk_Lot_No VARCHAR(64),
            Process_2_Df_Blk VARCHAR(64),
            Process_2_Df_Blk_Lot_No VARCHAR(64),
            Process_2_Df_Ring VARCHAR(64),
            Process_2_Df_Ring_Lot_No VARCHAR(64),
            Process_2_Washer VARCHAR(64),
            Process_2_Washer_Lot_No VARCHAR(64),
            Process_2_Lock_Nut VARCHAR(64),
            Process_2_Lock_Nut_Lot_No VARCHAR(64),
            Process_2_ST VARCHAR(64),
            Process_2_Actual_Time VARCHAR(64),
            Process_2_NG_Cause VARCHAR(64),
            Process_2_Repaired_Action VARCHAR(64)
        )
        """)
    
def CreateProcess3Table():
    global create_cursor

    create_cursor.execute("""
        CREATE TABLE IF NOT EXISTS process3_data(
            Process_3_DATA_No VARCHAR(64),
            Process_3_DateTime VARCHAR(64) PRIMARY KEY,
            Process_3_Model_Code VARCHAR(64),
            Process_3_S_N VARCHAR(64),
            Process_3_ID VARCHAR(64),
            Process_3_NAME VARCHAR(64),
            Process_3_Regular_Contractual VARCHAR(64),
            Process_3_Frame_Gasket VARCHAR(64),
            Process_3_Frame_Gasket_Lot_No VARCHAR(64),
            Process_3_Casing_Block VARCHAR(64),
            Process_3_Casing_Block_Lot_No VARCHAR(64),
            Process_3_Casing_Gasket VARCHAR(64),
            Process_3_Casing_Gasket_Lot_No VARCHAR(64),
            Process_3_M4x16_Screw_1 VARCHAR(64),
            Process_3_M4x16_Screw_1_Lot_No VARCHAR(64),
            Process_3_M4x16_Screw_2 VARCHAR(64),
            Process_3_M4x16_Screw_2_Lot_No VARCHAR(64),
            Process_3_Ball_Cushion VARCHAR(64),
            Process_3_Ball_Cushion_Lot_No VARCHAR(64),
            Process_3_Frame_Cover VARCHAR(64),
            Process_3_Frame_Cover_Lot_No VARCHAR(64),
            Process_3_Partition_Board VARCHAR(64),
            Process_3_Partition_Board_Lot_No VARCHAR(64),
            Process_3_Built_In_Tube_1 VARCHAR(64),
            Process_3_Built_In_Tube_1_Lot_No VARCHAR(64),
            Process_3_Built_In_Tube_2 VARCHAR(64),
            Process_3_Built_In_Tube_2_Lot_No VARCHAR(64),
            Process_3_Head_Cover VARCHAR(64),
            Process_3_Head_Cover_Lot_No VARCHAR(64),
            Process_3_Casing_Packing VARCHAR(64),
            Process_3_Casing_Packing_Lot_No VARCHAR(64),
            Process_3_M4x12_Screw VARCHAR(64),
            Process_3_M4x12_Screw_Lot_No VARCHAR(64),
            Process_3_Csb_L VARCHAR(64),
            Process_3_Csb_L_Lot_No VARCHAR(64),
            Process_3_Csb_R VARCHAR(64),
            Process_3_Csb_R_Lot_No VARCHAR(64),
            Process_3_Head_Packing VARCHAR(64),
            Process_3_Head_Packing_Lot_No VARCHAR(64),
            Process_3_ST VARCHAR(64),
            Process_3_Actual_Time VARCHAR(64),
            Process_3_NG_Cause VARCHAR(64),
            Process_3_Repaired_Action VARCHAR(64)
        )
        """)
    
def CreateProcess4Table():
    global create_cursor

    create_cursor.execute("""
        CREATE TABLE IF NOT EXISTS process4_data(
            Process_4_DATA_No VARCHAR(64),
            Process_4_DateTime VARCHAR(64) PRIMARY KEY,
            Process_4_Model_Code VARCHAR(64),
            Process_4_S_N VARCHAR(64),
            Process_4_ID VARCHAR(64),
            Process_4_NAME VARCHAR(64),
            Process_4_Regular_Contractual VARCHAR(64),
            Process_4_Tank VARCHAR(64),
            Process_4_Tank_Lot_No VARCHAR(64),
            Process_4_Upper_Housing VARCHAR(64),
            Process_4_Upper_Housing_Lot_No VARCHAR(64),
            Process_4_Cord_Hook VARCHAR(64),
            Process_4_Cord_Hook_Lot_No VARCHAR(64),
            Process_4_M4x16_Screw VARCHAR(64),
            Process_4_M4x16_Screw_Lot_No VARCHAR(64),
            Process_4_Tank_Gasket VARCHAR(64),
            Process_4_Tank_Gasket_Lot_No VARCHAR(64),
            Process_4_Tank_Cover VARCHAR(64),
            Process_4_Tank_Cover_Lot_No VARCHAR(64),
            Process_4_Housing_Gasket VARCHAR(64),
            Process_4_Housing_Gasket_Lot_No VARCHAR(64),
            Process_4_M4x40_Screw VARCHAR(64),
            Process_4_M4x40_Screw_Lot_No VARCHAR(64),
            Process_4_PartitionGasket VARCHAR(64),
            Process_4_PartitionGasket_Lot_No VARCHAR(64),
            Process_4_M4x12_Screw VARCHAR(64),
            Process_4_M4x12_Screw_Lot_No VARCHAR(64),
            Process_4_Muffler VARCHAR(64),
            Process_4_Muffler_Lot_No VARCHAR(64),
            Process_4_Muffler_Gasket VARCHAR(64),
            Process_4_Muffler_Gasket_Lot_No VARCHAR(64),
            Process_4_VCR VARCHAR(64),
            Process_4_VCR_Lot_No VARCHAR(64),
            Process_4_ST VARCHAR(64),
            Process_4_Actual_Time VARCHAR(64),
            Process_4_NG_Cause VARCHAR(64),
            Process_4_Repaired_Action VARCHAR(64)
        )
        """)
    
def CreateProcess5Table():
    global create_cursor

    create_cursor.execute("""
        CREATE TABLE IF NOT EXISTS process5_data(
            Process_5_DATA_No VARCHAR(64),
            Process_5_DateTime VARCHAR(64) PRIMARY KEY,
            Process_5_Model_Code VARCHAR(64),
            Process_5_S_N VARCHAR(64),
            Process_5_ID VARCHAR(64),
            Process_5_NAME VARCHAR(64),
            Process_5_Regular_Contractual VARCHAR(64),
            Process_5_Rating_Label VARCHAR(64),
            Process_5_Rating_Label_Lot_No VARCHAR(64),
            Process_5_ST VARCHAR(64),
            Process_5_Actual_Time VARCHAR(64),
            Process_5_NG_Cause VARCHAR(64),
            Process_5_Repaired_Action VARCHAR(64)
        )
        """)
    
def CreateProcess6Table():
    global create_cursor

    create_cursor.execute("""
        CREATE TABLE IF NOT EXISTS process6_data(
            Process_6_DATA_No VARCHAR(64),
            Process_6_DateTime VARCHAR(64) PRIMARY KEY,
            Process_6_Model_Code VARCHAR(64),
            Process_6_S_N VARCHAR(64),
            Process_6_ID VARCHAR(64),
            Process_6_NAME VARCHAR(64),
            Process_6_Regular_Contractual VARCHAR(64),
            Process_6_Vinyl VARCHAR(64),
            Process_6_Vinyl_Lot_No VARCHAR(64),
            Process_6_ST VARCHAR(64),
            Process_6_Actual_Time VARCHAR(64),
            Process_6_NG_Cause VARCHAR(64),
            Process_6_Repaired_Action VARCHAR(64)
        )
        """)
    
def CreateProcessTrialTable():
    global create_cursor

    create_cursor.execute("""
        CREATE TABLE IF NOT EXISTS trial_data(
            DATE VARCHAR(64),
            TIME VARCHAR(64),
            MODEL_CODE VARCHAR(64),
            PROCESS_S_N VARCHAR(64),
            S_N VARCHAR(64),
            PASS_NG VARCHAR(64),
            VOLTAGE_MAX_V VARCHAR(64),
            WATTAGE_MAX_W VARCHAR(64),
            CLOSED_PRESSURE_MAX_kPa VARCHAR(64),
            VOLTAGE_Middle_V VARCHAR(64),
            WATTAGE_Middle_W VARCHAR(64),
            AMPERAGE_Middle_A VARCHAR(64),
            CLOSED_PRESSURE_Middle_kPa VARCHAR(64),
            VOLTAGE_MIN_V VARCHAR(64),
            WATTAGE_MIN_W VARCHAR(64),
            CLOSED_PRESSURE_MIN_kPa VARCHAR(64),
            Process_1_S_N VARCHAR(64),
            Process_1_ID VARCHAR(64),
            Process_1_NAME VARCHAR(64),
            Process_1_Em2p VARCHAR(64),
            Process_1_Em2p_Lot_No VARCHAR(64),
            Process_1_Em2p_Inspection_3_Average_Data VARCHAR(64),
            Process_1_Em2p_Inspection_4_Average_Data VARCHAR(64),
            Process_1_Em2p_Inspection_5_Average_Data VARCHAR(64),
            Process_1_Em2p_Inspection_10_Average_Data VARCHAR(64),
            Process_1_Em2p_Inspection_3_Minimum_Data VARCHAR(64),
            Process_1_Em2p_Inspection_4_Minimum_Data VARCHAR(64),
            Process_1_Em2p_Inspection_5_Minimum_Data VARCHAR(64),
            Process_1_Em2p_Inspection_3_Maximum_Data VARCHAR(64),
            Process_1_Em2p_Inspection_4_Maximum_Data VARCHAR(64),
            Process_1_Em2p_Inspection_5_Maximum_Data VARCHAR(64),
            Process_1_Em3p VARCHAR(64),
            Process_1_Em3p_Lot_No VARCHAR(64),
            Process_1_Em3p_Inspection_3_Average_Data VARCHAR(64),
            Process_1_Em3p_Inspection_4_Average_Data VARCHAR(64),
            Process_1_Em3p_Inspection_5_Average_Data VARCHAR(64),
            Process_1_Em3p_Inspection_10_Average_Data VARCHAR(64),
            Process_1_Em3p_Inspection_3_Minimum_Data VARCHAR(64),
            Process_1_Em3p_Inspection_4_Minimum_Data VARCHAR(64),
            Process_1_Em3p_Inspection_5_Minimum_Data VARCHAR(64),
            Process_1_Em3p_Inspection_3_Maximum_Data VARCHAR(64),
            Process_1_Em3p_Inspection_4_Maximum_Data VARCHAR(64),
            Process_1_Em3p_Inspection_5_Maximum_Data VARCHAR(64),
            Process_1_Harness VARCHAR(64),
            Process_1_Harness_Lot_No VARCHAR(64),
            Process_1_Frame VARCHAR(64),
            Process_1_Frame_Lot_No VARCHAR(64),
            Process_1_Frame_Inspection_1_Average_Data VARCHAR(64),
            Process_1_Frame_Inspection_2_Average_Data VARCHAR(64),
            Process_1_Frame_Inspection_3_Average_Data VARCHAR(64),
            Process_1_Frame_Inspection_4_Average_Data VARCHAR(64),
            Process_1_Frame_Inspection_5_Average_Data VARCHAR(64),
            Process_1_Frame_Inspection_6_Average_Data VARCHAR(64),
            Process_1_Frame_Inspection_7_Average_Data VARCHAR(64),
            Process_1_Frame_Inspection_1_Minimum_Data VARCHAR(64),
            Process_1_Frame_Inspection_2_Minimum_Data VARCHAR(64),
            Process_1_Frame_Inspection_3_Minimum_Data VARCHAR(64),
            Process_1_Frame_Inspection_4_Minimum_Data VARCHAR(64),
            Process_1_Frame_Inspection_5_Minimum_Data VARCHAR(64),
            Process_1_Frame_Inspection_6_Minimum_Data VARCHAR(64),
            Process_1_Frame_Inspection_7_Minimum_Data VARCHAR(64),
            Process_1_Frame_Inspection_1_Maximum_Data VARCHAR(64),
            Process_1_Frame_Inspection_2_Maximum_Data VARCHAR(64),
            Process_1_Frame_Inspection_3_Maximum_Data VARCHAR(64),
            Process_1_Frame_Inspection_4_Maximum_Data VARCHAR(64),
            Process_1_Frame_Inspection_5_Maximum_Data VARCHAR(64),
            Process_1_Frame_Inspection_6_Maximum_Data VARCHAR(64),
            Process_1_Frame_Inspection_7_Maximum_Data VARCHAR(64),
            Process_1_Bushing VARCHAR(64),
            Process_1_Bushing_Lot_No VARCHAR(64),
            Process_1_ST VARCHAR(64),
            Process_1_Actual_Time VARCHAR(64),
            Process_1_NG_Cause VARCHAR(64),
            Process_1_Repaired_Action VARCHAR(64),
            Process_2_S_N VARCHAR(64),
            Process_2_ID VARCHAR(64),
            Process_2_NAME VARCHAR(64),
            Process_2_M4x40_Screw VARCHAR(64),
            Process_2_M4x40_Screw_Lot_No VARCHAR(64),
            Process_2_Rod_Blk VARCHAR(64),
            Process_2_Rod_Blk_Lot_No VARCHAR(64),
            Process_2_Rod_Blk_Tesla_1_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Tesla_2_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Tesla_3_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Tesla_4_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Tesla_1_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Tesla_2_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Tesla_3_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Tesla_4_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Tesla_1_Maximum_Data VARCHAR(64),
            Process_2_Rod_Blk_Tesla_2_Maximum_Data VARCHAR(64),
            Process_2_Rod_Blk_Tesla_3_Maximum_Data VARCHAR(64),
            Process_2_Rod_Blk_Tesla_4_Maximum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_1_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_2_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_3_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_4_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_5_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_6_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_7_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_8_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_9_Average_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_1_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_2_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_3_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_4_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_5_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_6_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_7_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_8_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_9_Minimum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_1_Maximum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_2_Maximum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_3_Maximum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_4_Maximum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_5_Maximum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_6_Maximum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_7_Maximum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_8_Maximum_Data VARCHAR(64),
            Process_2_Rod_Blk_Inspection_9_Maximum_Data VARCHAR(64),
            Process_2_Df_Blk VARCHAR(64),
            Process_2_Df_Blk_Lot_No VARCHAR(64),
            Process_2_Df_Blk_Inspection_1_Average_Data VARCHAR(64),
            Process_2_Df_Blk_Inspection_2_Average_Data VARCHAR(64),
            Process_2_Df_Blk_Inspection_3_Average_Data VARCHAR(64),
            Process_2_Df_Blk_Inspection_4_Average_Data VARCHAR(64),
            Process_2_Df_Blk_Inspection_1_Minimum_Data VARCHAR(64),
            Process_2_Df_Blk_Inspection_2_Minimum_Data VARCHAR(64),
            Process_2_Df_Blk_Inspection_3_Minimum_Data VARCHAR(64),
            Process_2_Df_Blk_Inspection_4_Minimum_Data VARCHAR(64),
            Process_2_Df_Blk_Inspection_1_Maximum_Data VARCHAR(64),
            Process_2_Df_Blk_Inspection_2_Maximum_Data VARCHAR(64),
            Process_2_Df_Blk_Inspection_3_Maximum_Data VARCHAR(64),
            Process_2_Df_Blk_Inspection_4_Maximum_Data VARCHAR(64),
            Process_2_Df_Blk_Tensile_Rate_Of_Change_Average VARCHAR(64),
            Process_2_Df_Blk_Tensile_Rate_Of_Change_Minimum VARCHAR(64),
            Process_2_Df_Blk_Tensile_Rate_Of_Change_Maximum VARCHAR(64),
            Process_2_Df_Blk_Tensile_Start_Force_Average VARCHAR(64),
            Process_2_Df_Blk_Tensile_Start_Force_Minimum VARCHAR(64),
            Process_2_Df_Blk_Tensile_Start_Force_Maximum VARCHAR(64),
            Process_2_Df_Blk_Tensile_Terminating_Force_Average VARCHAR(64),
            Process_2_Df_Blk_Tensile_Terminating_Force_Minimum VARCHAR(64),
            Process_2_Df_Blk_Tensile_Terminating_Force_Maximum VARCHAR(64),
            Process_2_Df_Ring VARCHAR(64),
            Process_2_Df_Ring_Lot_No VARCHAR(64),
            Process_2_Washer VARCHAR(64),
            Process_2_Washer_Lot_No VARCHAR(64),
            Process_2_Lock_Nut VARCHAR(64),
            Process_2_Lock_Nut_Lot_No VARCHAR(64),
            Process_2_ST VARCHAR(64),
            Process_2_Actual_Time VARCHAR(64),
            Process_2_NG_Cause VARCHAR(64),
            Process_2_Repaired_Action VARCHAR(64),
            Process_3_S_N VARCHAR(64),
            Process_3_ID VARCHAR(64),
            Process_3_NAME VARCHAR(64),
            Process_3_Frame_Gasket VARCHAR(64),
            Process_3_Frame_Gasket_Lot_No VARCHAR(64),
            Process_3_Casing_Block VARCHAR(64),
            Process_3_Casing_Block_Lot_No VARCHAR(64),
            Process_3_Casing_Block_Inspection_1_Average_Data VARCHAR(64),
            Process_3_Casing_Block_Inspection_1_Minimum_Data VARCHAR(64),
            Process_3_Casing_Block_Inspection_1_Maximum_Data VARCHAR(64),
            Process_3_Casing_Gasket VARCHAR(64),
            Process_3_Casing_Gasket_Lot_No VARCHAR(64),
            Process_3_M4x16_Screw_1 VARCHAR(64),
            Process_3_M4x16_Screw_1_Lot_No VARCHAR(64),
            Process_3_M4x16_Screw_2 VARCHAR(64),
            Process_3_M4x16_Screw_2_Lot_No VARCHAR(64),
            Process_3_Ball_Cushion VARCHAR(64),
            Process_3_Ball_Cushion_Lot_No VARCHAR(64),
            Process_3_Frame_Cover VARCHAR(64),
            Process_3_Frame_Cover_Lot_No VARCHAR(64),
            Process_3_Partition_Board VARCHAR(64),
            Process_3_Partition_Board_Lot_No VARCHAR(64),
            Process_3_Built_In_Tube_1 VARCHAR(64),
            Process_3_Built_In_Tube_1_Lot_No VARCHAR(64),
            Process_3_Built_In_Tube_2 VARCHAR(64),
            Process_3_Built_In_Tube_2_Lot_No VARCHAR(64),
            Process_3_Head_Cover VARCHAR(64),
            Process_3_Head_Cover_Lot_No VARCHAR(64),
            Process_3_Casing_Packing VARCHAR(64),
            Process_3_Casing_Packing_Lot_No VARCHAR(64),
            Process_3_M4x12_Screw VARCHAR(64),
            Process_3_M4x12_Screw_Lot_No VARCHAR(64),
            Process_3_Csb_L VARCHAR(64),
            Process_3_Csb_L_Lot_No VARCHAR(64),
            Process_3_Csb_R VARCHAR(64),
            Process_3_Csb_R_Lot_No VARCHAR(64),
            Process_3_Head_Packing VARCHAR(64),
            Process_3_Head_Packing_Lot_No VARCHAR(64),
            Process_3_ST VARCHAR(64),
            Process_3_Actual_Time VARCHAR(64),
            Process_3_NG_Cause VARCHAR(64),
            Process_3_Repaired_Action VARCHAR(64),
            Process_4_S_N VARCHAR(64),
            Process_4_ID VARCHAR(64),
            Process_4_NAME VARCHAR(64),
            Process_4_Tank VARCHAR(64),
            Process_4_Tank_Lot_No VARCHAR(64),
            Process_4_Upper_Housing VARCHAR(64),
            Process_4_Upper_Housing_Lot_No VARCHAR(64),
            Process_4_Cord_Hook VARCHAR(64),
            Process_4_Cord_Hook_Lot_No VARCHAR(64),
            Process_4_M4x16_Screw VARCHAR(64),
            Process_4_M4x16_Screw_Lot_No VARCHAR(64),
            Process_4_Tank_Gasket VARCHAR(64),
            Process_4_Tank_Gasket_Lot_No VARCHAR(64),
            Process_4_Tank_Cover VARCHAR(64),
            Process_4_Tank_Cover_Lot_No VARCHAR(64),
            Process_4_Housing_Gasket VARCHAR(64),
            Process_4_Housing_Gasket_Lot_No VARCHAR(64),
            Process_4_M4x40_Screw VARCHAR(64),
            Process_4_M4x40_Screw_Lot_No VARCHAR(64),
            Process_4_PartitionGasket VARCHAR(64),
            Process_4_PartitionGasket_Lot_No VARCHAR(64),
            Process_4_M4x12_Screw VARCHAR(64),
            Process_4_M4x12_Screw_Lot_No VARCHAR(64),
            Process_4_Muffler VARCHAR(64),
            Process_4_Muffler_Lot_No VARCHAR(64),
            Process_4_Muffler_Gasket VARCHAR(64),
            Process_4_Muffler_Gasket_Lot_No VARCHAR(64),
            Process_4_VCR VARCHAR(64),
            Process_4_VCR_Lot_No VARCHAR(64),
            Process_4_ST VARCHAR(64),
            Process_4_Actual_Time VARCHAR(64),
            Process_4_NG_Cause VARCHAR(64),
            Process_4_Repaired_Action VARCHAR(64),
            Process_5_S_N VARCHAR(64),
            Process_5_ID VARCHAR(64),
            Process_5_NAME VARCHAR(64),
            Process_5_Rating_Label VARCHAR(64),
            Process_5_Rating_Label_Lot_No VARCHAR(64),
            Process_5_ST VARCHAR(64),
            Process_5_Actual_Time VARCHAR(64),
            Process_5_NG_Cause VARCHAR(64),
            Process_5_Repaired_Action VARCHAR(64),
            Process_6_S_N VARCHAR(64),
            Process_6_ID VARCHAR(64),
            Process_6_NAME VARCHAR(64),
            Process_6_Vinyl VARCHAR(64),
            Process_6_Vinyl_Lot_No VARCHAR(64),
            Process_6_ST VARCHAR(64),
            Process_6_Actual_Time VARCHAR(64),
            Process_6_NG_Cause VARCHAR(64),
            Process_6_Repaired_Action VARCHAR(64)
        )
        """)
    
def CreateFC1InspectionMachineTable():
    global create_cursor

    create_cursor.execute("""
        CREATE TABLE IF NOT EXISTS inspection_machine_data(
            DATETIME DATETIME PRIMARY KEY,
            DATE DATE,
            TIME TIME,
            MODEL_CODE VARCHAR(64),
            S_N VARCHAR(64),
            PASS_NG VARCHAR(64),
            VOLTAGE_MAX_V FLOAT,
            WATTAGE_MAX_W FLOAT,
            CLOSED_PRESSURE_MAX_kPa FLOAT,
            VOLTAGE_Middle_V FLOAT,
            WATTAGE_Middle_W FLOAT,
            AMPERAGE_Middle_A FLOAT,
            CLOSED_PRESSURE_Middle_kPa FLOAT,
            VOLTAGE_MIN_V FLOAT,
            WATTAGE_MIN_W FLOAT,
            CLOSED_PRESSURE_MIN_kPa FLOAT
        )
        """)
    
def CreateFC1UclLclTable():
    global create_cursor

    create_cursor.execute("""
        CREATE TABLE IF NOT EXISTS ucl_lcl_data(
            DATETIME DATETIME PRIMARY KEY,
            MODEL_CODE VARCHAR(64),
            S_N VARCHAR(64),
            VOLTAGE_MAX_V VARCHAR(64),
            VOLTAGE_MAX_V_UCL VARCHAR(64),
            VOLTAGE_MAX_V_LCL VARCHAR(64),
            VOLTAGE_MAX_V_REMARKS VARCHAR(64),
            WATTAGE_MAX_W VARCHAR(64),
            WATTAGE_MAX_W_UCL VARCHAR(64),
            WATTAGE_MAX_W_LCL VARCHAR(64),
            WATTAGE_MAX_W_REMARKS VARCHAR(64),
            CLOSED_PRESSURE_MAX_kPa VARCHAR(64),
            CLOSED_PRESSURE_MAX_kPa_UCL VARCHAR(64),
            CLOSED_PRESSURE_MAX_kPa_LCL VARCHAR(64),
            CLOSED_PRESSURE_MAX_kPa_REMARKS VARCHAR(64),
            VOLTAGE_Middle_V VARCHAR(64),
            VOLTAGE_Middle_V_UCL VARCHAR(64),
            VOLTAGE_Middle_V_LCL VARCHAR(64),
            VOLTAGE_Middle_V_REMARKS VARCHAR(64),
            WATTAGE_Middle_W VARCHAR(64),
            WATTAGE_Middle_W_UCL VARCHAR(64),
            WATTAGE_Middle_W_LCL VARCHAR(64),
            WATTAGE_Middle_W_REMARKS VARCHAR(64),
            AMPERAGE_Middle_A VARCHAR(64),
            AMPERAGE_Middle_A_UCL VARCHAR(64),
            AMPERAGE_Middle_A_LCL VARCHAR(64),
            AMPERAGE_Middle_A_REMARKS VARCHAR(64),
            CLOSED_PRESSURE_Middle_kPa VARCHAR(64),
            CLOSED_PRESSURE_Middle_kPa_UCL VARCHAR(64),
            CLOSED_PRESSURE_Middle_kPa_LCL VARCHAR(64),
            CLOSED_PRESSURE_Middle_kPa_REMARKS VARCHAR(64),
            VOLTAGE_MIN_V VARCHAR(64),
            VOLTAGE_MIN_V_UCL VARCHAR(64),
            VOLTAGE_MIN_V_LCL VARCHAR(64),
            VOLTAGE_MIN_V_REMARKS VARCHAR(64),
            WATTAGE_MIN_W VARCHAR(64),
            WATTAGE_MIN_W_UCL VARCHAR(64),
            WATTAGE_MIN_W_LCL VARCHAR(64),
            WATTAGE_MIN_W_REMARKS VARCHAR(64),
            CLOSED_PRESSURE_MIN_kPa VARCHAR(64),
            CLOSED_PRESSURE_MIN_kPa_UCL VARCHAR(64),
            CLOSED_PRESSURE_MIN_kPa_LCL VARCHAR(64),
            CLOSED_PRESSURE_MIN_kPa_REMARKS VARCHAR(64)
        )
        """)

def ShowTables():
    global create_cursor

    create_cursor.execute("SHOW TABLES")

    for x in create_cursor:
        print(x)

def DeleteTable(tableName):
    global create_cursor
    
    create_cursor.execute(f"DROP TABLE IF EXISTS {tableName}")

def DeleteDataFromDatabaseData(date):
    global create_cursor, mariadb_connection

    create_cursor.execute(f"DELETE FROM database_data WHERE DATE = '{date}'")
    mariadb_connection.commit()

def InsertDataToTable(tableName):
    global create_cursor, mariadb_connection
    
    sqlStatement = f"INSERT INTO {tableName} (Name, Date, MODELCODE) VALUES ('CARL', '29/05/2025', '213P')"
    create_cursor.execute(sqlStatement)
    mariadb_connection.commit()

def InsertDataToTable2(tableName):
    global create_cursor, mariadb_connection

    sqlStatement = f"INSERT INTO {tableName} (Name, Date, MODELCODE) VALUES (%s, %s, %s)"
    itemsToInsert = ['CARL', '29/05/2025', '213P']

    create_cursor.execute(sqlStatement, itemsToInsert)
    mariadb_connection.commit()

def InsertDataToProcess1Table(df):
    global create_cursor, mariadb_connection

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    
    # First, get all existing datetimes from the database
    create_cursor.execute("SELECT Process_1_DateTime FROM process1_data")
    existing_datetimes = [row[0] for row in create_cursor.fetchall()]
    
    # Filter out records that already exist in the database
    new_records = []
    for record in df.values.tolist():
        if str(record[1]) not in existing_datetimes:  # Process_1_DateTime is at index 1
            new_records.append(record)
    
    if not new_records:
        print("No new records to insert")
        return
    
    # Create the SQL insert statement
    insert_query = """
        INSERT INTO process1_data (
            Process_1_DATA_No,
            Process_1_DateTime,
            Process_1_Model_Code,
            Process_1_S_N,
            Process_1_ID,
            Process_1_NAME,
            Process_1_Regular_Contractual,
            Process_1_Em2p,
            Process_1_Em2p_Lot_No,
            Process_1_Em3p,
            Process_1_Em3p_Lot_No,
            Process_1_Harness,
            Process_1_Harness_Lot_No,
            Process_1_Frame,
            Process_1_Frame_Lot_No,
            Process_1_Bushing,
            Process_1_Bushing_Lot_No,
            Process_1_ST,
            Process_1_Actual_Time,
            Process_1_NG_Cause,
            Process_1_Repaired_Action
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Execute the insert only for new records
    create_cursor.executemany(insert_query, new_records)
    mariadb_connection.commit()
    print(f"Successfully inserted {len(new_records)} new records into process1_data table")

def InsertDataToProcess2Table(df):
    global create_cursor, mariadb_connection

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    
    # First, get all existing datetimes from the database
    create_cursor.execute("SELECT Process_2_DateTime FROM process2_data")
    existing_datetimes = [row[0] for row in create_cursor.fetchall()]
    
    # Filter out records that already exist in the database
    new_records = []
    for record in df.values.tolist():
        if str(record[1]) not in existing_datetimes:  # Process_1_DateTime is at index 1
            new_records.append(record)
    
    if not new_records:
        print("No new records to insert")
        return
    
    # Create the SQL insert statement
    insert_query = """
        INSERT INTO process2_data (
            Process_2_DATA_No,
            Process_2_DateTime,
            Process_2_Model_Code,
            Process_2_S_N,
            Process_2_ID,
            Process_2_NAME,
            Process_2_Regular_Contractual,
            Process_2_M4x40_Screw,
            Process_2_M4x40_Screw_Lot_No,
            Process_2_Rod_Blk,
            Process_2_Rod_Blk_Lot_No,
            Process_2_Df_Blk,
            Process_2_Df_Blk_Lot_No,
            Process_2_Df_Ring,
            Process_2_Df_Ring_Lot_No,
            Process_2_Washer,
            Process_2_Washer_Lot_No,
            Process_2_Lock_Nut,
            Process_2_Lock_Nut_Lot_No,
            Process_2_ST,
            Process_2_Actual_Time,
            Process_2_NG_Cause,
            Process_2_Repaired_Action
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Execute the insert only for new records
    create_cursor.executemany(insert_query, new_records)
    mariadb_connection.commit()
    print(f"Successfully inserted {len(new_records)} new records into process2_data table")

def InsertDataToProcess3Table(df):
    global create_cursor, mariadb_connection

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    
    # First, get all existing datetimes from the database
    create_cursor.execute("SELECT Process_3_DateTime FROM process3_data")
    existing_datetimes = [row[0] for row in create_cursor.fetchall()]
    
    # Filter out records that already exist in the database
    new_records = []
    for record in df.values.tolist():
        if str(record[1]) not in existing_datetimes:  # Process_1_DateTime is at index 1
            new_records.append(record)
    
    if not new_records:
        print("No new records to insert")
        return
    
    # Create the SQL insert statement
    insert_query = """
        INSERT INTO process3_data (
            Process_3_DATA_No,
            Process_3_DateTime,
            Process_3_Model_Code,
            Process_3_S_N,
            Process_3_ID,
            Process_3_NAME,
            Process_3_Regular_Contractual,
            Process_3_Frame_Gasket,
            Process_3_Frame_Gasket_Lot_No,
            Process_3_Casing_Block,
            Process_3_Casing_Block_Lot_No,
            Process_3_Casing_Gasket,
            Process_3_Casing_Gasket_Lot_No,
            Process_3_M4x16_Screw_1,
            Process_3_M4x16_Screw_1_Lot_No,
            Process_3_M4x16_Screw_2,
            Process_3_M4x16_Screw_2_Lot_No,
            Process_3_Ball_Cushion,
            Process_3_Ball_Cushion_Lot_No,
            Process_3_Frame_Cover,
            Process_3_Frame_Cover_Lot_No,
            Process_3_Partition_Board,
            Process_3_Partition_Board_Lot_No,
            Process_3_Built_In_Tube_1,
            Process_3_Built_In_Tube_1_Lot_No,
            Process_3_Built_In_Tube_2,
            Process_3_Built_In_Tube_2_Lot_No,
            Process_3_Head_Cover,
            Process_3_Head_Cover_Lot_No,
            Process_3_Casing_Packing,
            Process_3_Casing_Packing_Lot_No,
            Process_3_M4x12_Screw,
            Process_3_M4x12_Screw_Lot_No,
            Process_3_Csb_L,
            Process_3_Csb_L_Lot_No,
            Process_3_Csb_R,
            Process_3_Csb_R_Lot_No,
            Process_3_Head_Packing,
            Process_3_Head_Packing_Lot_No,
            Process_3_ST,
            Process_3_Actual_Time,
            Process_3_NG_Cause,
            Process_3_Repaired_Action
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Execute the insert only for new records
    create_cursor.executemany(insert_query, new_records)
    mariadb_connection.commit()
    print(f"Successfully inserted {len(new_records)} new records into process3_data table")

def InsertDataToProcess4Table(df):
    global create_cursor, mariadb_connection

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    
    # First, get all existing datetimes from the database
    create_cursor.execute("SELECT Process_4_DateTime FROM process4_data")
    existing_datetimes = [row[0] for row in create_cursor.fetchall()]
    
    # Filter out records that already exist in the database
    new_records = []
    for record in df.values.tolist():
        if str(record[1]) not in existing_datetimes:  # Process_1_DateTime is at index 1
            new_records.append(record)
    
    if not new_records:
        print("No new records to insert")
        return
    
    # Create the SQL insert statement
    insert_query = """
        INSERT INTO process4_data (
            Process_4_DATA_No,
            Process_4_DateTime,
            Process_4_Model_Code,
            Process_4_S_N,
            Process_4_ID,
            Process_4_NAME,
            Process_4_Regular_Contractual,
            Process_4_Tank,
            Process_4_Tank_Lot_No,
            Process_4_Upper_Housing,
            Process_4_Upper_Housing_Lot_No,
            Process_4_Cord_Hook,
            Process_4_Cord_Hook_Lot_No,
            Process_4_M4x16_Screw,
            Process_4_M4x16_Screw_Lot_No,
            Process_4_Tank_Gasket,
            Process_4_Tank_Gasket_Lot_No,
            Process_4_Tank_Cover,
            Process_4_Tank_Cover_Lot_No,
            Process_4_Housing_Gasket,
            Process_4_Housing_Gasket_Lot_No,
            Process_4_M4x40_Screw,
            Process_4_M4x40_Screw_Lot_No,
            Process_4_PartitionGasket,
            Process_4_PartitionGasket_Lot_No,
            Process_4_M4x12_Screw,
            Process_4_M4x12_Screw_Lot_No,
            Process_4_Muffler,
            Process_4_Muffler_Lot_No,
            Process_4_Muffler_Gasket,
            Process_4_Muffler_Gasket_Lot_No,
            Process_4_VCR,
            Process_4_VCR_Lot_No,
            Process_4_ST,
            Process_4_Actual_Time,
            Process_4_NG_Cause,
            Process_4_Repaired_Action
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Execute the insert only for new records
    create_cursor.executemany(insert_query, new_records)
    mariadb_connection.commit()
    print(f"Successfully inserted {len(new_records)} new records into process4_data table")

def InsertDataToProcess5Table(df):
    global create_cursor, mariadb_connection

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    
    # First, get all existing datetimes from the database
    create_cursor.execute("SELECT Process_5_DateTime FROM process5_data")
    existing_datetimes = [row[0] for row in create_cursor.fetchall()]
    
    # Filter out records that already exist in the database
    new_records = []
    for record in df.values.tolist():
        if str(record[1]) not in existing_datetimes:  # Process_1_DateTime is at index 1
            new_records.append(record)
    
    if not new_records:
        print("No new records to insert")
        return
    
    # Create the SQL insert statement
    insert_query = """
        INSERT INTO process5_data (
            Process_5_DATA_No,
            Process_5_DateTime,
            Process_5_Model_Code,
            Process_5_S_N,
            Process_5_ID,
            Process_5_NAME,
            Process_5_Regular_Contractual,
            Process_5_Rating_Label,
            Process_5_Rating_Label_Lot_No,
            Process_5_ST,
            Process_5_Actual_Time,
            Process_5_NG_Cause,
            Process_5_Repaired_Action
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Execute the insert only for new records
    create_cursor.executemany(insert_query, new_records)
    mariadb_connection.commit()
    print(f"Successfully inserted {len(new_records)} new records into process5_data table")

def InsertDataToProcess6Table(df):
    global create_cursor, mariadb_connection

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    
    # First, get all existing datetimes from the database
    create_cursor.execute("SELECT Process_6_DateTime FROM process6_data")
    existing_datetimes = [row[0] for row in create_cursor.fetchall()]
    
    # Filter out records that already exist in the database
    new_records = []
    for record in df.values.tolist():
        if str(record[1]) not in existing_datetimes:  # Process_1_DateTime is at index 1
            new_records.append(record)
    
    if not new_records:
        print("No new records to insert")
        return
    
    # Create the SQL insert statement
    insert_query = """
        INSERT INTO process6_data (
            Process_6_DATA_No,
            Process_6_DateTime,
            Process_6_Model_Code,
            Process_6_S_N,
            Process_6_ID,
            Process_6_NAME,
            Process_6_Regular_Contractual,
            Process_6_Vinyl,
            Process_6_Vinyl_Lot_No,
            Process_6_ST,
            Process_6_Actual_Time,
            Process_6_NG_Cause,
            Process_6_Repaired_Action
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Execute the insert only for new records
    create_cursor.executemany(insert_query, new_records)
    mariadb_connection.commit()
    print(f"Successfully inserted {len(new_records)} new records into process6_data table")

def InsertDataToFC1InspectionMachineTable(df):
    global create_cursor, mariadb_connection

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    
    # First, get all existing datetimes from the database
    create_cursor.execute("SELECT DATETIME FROM inspection_machine_data")
    existing_datetimes = [str(row[0]) for row in create_cursor.fetchall()]
    
    # Filter out records that already exist in the database
    new_records = []
    for record in df.values.tolist():
        if str(record[0]) not in existing_datetimes:  # Process_1_DateTime is at index 1
            new_records.append(record)
    
    if not new_records:
        print("No new records to insert")
        return
    
    # Create the SQL insert statement
    insert_query = """
        INSERT INTO inspection_machine_data (
            DATETIME,
            DATE,
            TIME,
            MODEL_CODE,
            S_N,
            PASS_NG,
            VOLTAGE_MAX_V,
            WATTAGE_MAX_W,
            CLOSED_PRESSURE_MAX_kPa,
            VOLTAGE_Middle_V,
            WATTAGE_Middle_W,
            AMPERAGE_Middle_A,
            CLOSED_PRESSURE_Middle_kPa,
            VOLTAGE_MIN_V,
            WATTAGE_MIN_W,
            CLOSED_PRESSURE_MIN_kPa
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Execute the insert only for new records
    create_cursor.executemany(insert_query, new_records)
    mariadb_connection.commit()
    print(f"Successfully inserted {len(new_records)} new records into inspection_machine_data table")

def InsertDataToFC1UclLclTable(df):
    global create_cursor, mariadb_connection

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    
    # First, get all existing datetimes from the database
    create_cursor.execute("SELECT DATETIME FROM ucl_lcl_data")
    existing_datetimes = [str(row[0]) for row in create_cursor.fetchall()]
    
    # Filter out records that already exist in the database
    new_records = []
    for record in df.values.tolist():
        if str(record[0]) not in existing_datetimes:  # Process_1_DateTime is at index 1
            new_records.append(record)
    
    if not new_records:
        print("No new records to insert")
        return
    
    # Create the SQL insert statement
    insert_query = """
        INSERT INTO ucl_lcl_data (
            DATETIME,
            MODEL_CODE,
            S_N,
            VOLTAGE_MAX_V,
            VOLTAGE_MAX_V_UCL,
            VOLTAGE_MAX_V_LCL,
            VOLTAGE_MAX_V_REMARKS,
            WATTAGE_MAX_W,
            WATTAGE_MAX_W_UCL,
            WATTAGE_MAX_W_LCL,
            WATTAGE_MAX_W_REMARKS,
            CLOSED_PRESSURE_MAX_kPa,
            CLOSED_PRESSURE_MAX_kPa_UCL,
            CLOSED_PRESSURE_MAX_kPa_LCL,
            CLOSED_PRESSURE_MAX_kPa_REMARKS,
            VOLTAGE_Middle_V,
            VOLTAGE_Middle_V_UCL,
            VOLTAGE_Middle_V_LCL,
            VOLTAGE_Middle_V_REMARKS,
            WATTAGE_Middle_W,
            WATTAGE_Middle_W_UCL,
            WATTAGE_Middle_W_LCL,
            WATTAGE_Middle_W_REMARKS,
            AMPERAGE_Middle_A,
            AMPERAGE_Middle_A_UCL,
            AMPERAGE_Middle_A_LCL,
            AMPERAGE_Middle_A_REMARKS,
            CLOSED_PRESSURE_Middle_kPa,
            CLOSED_PRESSURE_Middle_kPa_UCL,
            CLOSED_PRESSURE_Middle_kPa_LCL,
            CLOSED_PRESSURE_Middle_kPa_REMARKS,
            VOLTAGE_MIN_V,
            VOLTAGE_MIN_V_UCL,
            VOLTAGE_MIN_V_LCL,
            VOLTAGE_MIN_V_REMARKS,
            WATTAGE_MIN_W,
            WATTAGE_MIN_W_UCL,
            WATTAGE_MIN_W_LCL,
            WATTAGE_MIN_W_REMARKS,
            CLOSED_PRESSURE_MIN_kPa,
            CLOSED_PRESSURE_MIN_kPa_UCL,
            CLOSED_PRESSURE_MIN_kPa_LCL,
            CLOSED_PRESSURE_MIN_kPa_REMARKS
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s
        )
    """
    
    # Execute the insert only for new records
    create_cursor.executemany(insert_query, new_records)
    mariadb_connection.commit()
    print(f"Successfully inserted {len(new_records)} new records into inspection_machine_data table")

def InsertDataToFC1DatabaseTable(df):
    global create_cursor, mariadb_connection

    # Replace NaN values with None
    df = df.replace({np.nan: None})
    
    # First, get all existing datetimes from the database
    create_cursor.execute("SELECT DATETIME FROM database_data")
    existing_datetimes = [str(row[0]) for row in create_cursor.fetchall()]
    
    # Filter out records that already exist in the database
    new_records = []
    for record in df.values.tolist():
        if str(record[0]) not in existing_datetimes:  # Process_1_DateTime is at index 1
            new_records.append(record)
    
    if not new_records:
        print("No new records to insert")
        return
    
    # Create the SQL insert statement
    insert_query = """
        INSERT INTO database_data (
            DATETIME,
            DATE,
            TIME,
            MODEL_CODE,
            PROCESS_S_N,
            S_N,
            PASS_NG,
            VOLTAGE_MAX_V,
            WATTAGE_MAX_W,
            CLOSED_PRESSURE_MAX_kPa,
            VOLTAGE_Middle_V,
            WATTAGE_Middle_W,
            AMPERAGE_Middle_A,
            CLOSED_PRESSURE_Middle_kPa,
            VOLTAGE_MIN_V,
            WATTAGE_MIN_W,
            CLOSED_PRESSURE_MIN_kPa,
            Process_1_S_N,
            Process_1_ID,
            Process_1_NAME,
            Process_1_Em2p,
            Process_1_Em2p_Lot_No,
            Process_1_Em2p_Inspection_3_Average_Data,
            Process_1_Em2p_Inspection_4_Average_Data,
            Process_1_Em2p_Inspection_5_Average_Data,
            Process_1_Em2p_Inspection_10_Average_Data,
            Process_1_Em2p_Inspection_3_Minimum_Data,
            Process_1_Em2p_Inspection_4_Minimum_Data,
            Process_1_Em2p_Inspection_5_Minimum_Data,
            Process_1_Em2p_Inspection_3_Maximum_Data,
            Process_1_Em2p_Inspection_4_Maximum_Data,
            Process_1_Em2p_Inspection_5_Maximum_Data,
            Process_1_Em3p,
            Process_1_Em3p_Lot_No,
            Process_1_Em3p_Inspection_3_Average_Data,
            Process_1_Em3p_Inspection_4_Average_Data,
            Process_1_Em3p_Inspection_5_Average_Data,
            Process_1_Em3p_Inspection_10_Average_Data,
            Process_1_Em3p_Inspection_3_Minimum_Data,
            Process_1_Em3p_Inspection_4_Minimum_Data,
            Process_1_Em3p_Inspection_5_Minimum_Data,
            Process_1_Em3p_Inspection_3_Maximum_Data,
            Process_1_Em3p_Inspection_4_Maximum_Data,
            Process_1_Em3p_Inspection_5_Maximum_Data,
            Process_1_Harness,
            Process_1_Harness_Lot_No,
            Process_1_Frame,
            Process_1_Frame_Lot_No,
            Process_1_Frame_Inspection_1_Average_Data,
            Process_1_Frame_Inspection_2_Average_Data,
            Process_1_Frame_Inspection_3_Average_Data,
            Process_1_Frame_Inspection_4_Average_Data,
            Process_1_Frame_Inspection_5_Average_Data,
            Process_1_Frame_Inspection_6_Average_Data,
            Process_1_Frame_Inspection_7_Average_Data,
            Process_1_Frame_Inspection_1_Minimum_Data,
            Process_1_Frame_Inspection_2_Minimum_Data,
            Process_1_Frame_Inspection_3_Minimum_Data,
            Process_1_Frame_Inspection_4_Minimum_Data,
            Process_1_Frame_Inspection_5_Minimum_Data,
            Process_1_Frame_Inspection_6_Minimum_Data,
            Process_1_Frame_Inspection_7_Minimum_Data,
            Process_1_Frame_Inspection_1_Maximum_Data,
            Process_1_Frame_Inspection_2_Maximum_Data,
            Process_1_Frame_Inspection_3_Maximum_Data,
            Process_1_Frame_Inspection_4_Maximum_Data,
            Process_1_Frame_Inspection_5_Maximum_Data,
            Process_1_Frame_Inspection_6_Maximum_Data,
            Process_1_Frame_Inspection_7_Maximum_Data,
            Process_1_Bushing,
            Process_1_Bushing_Lot_No,
            Process_1_ST,
            Process_1_Actual_Time,
            Process_1_NG_Cause,
            Process_1_Repaired_Action,
            Process_2_S_N,
            Process_2_ID,
            Process_2_NAME,
            Process_2_M4x40_Screw,
            Process_2_M4x40_Screw_Lot_No,
            Process_2_Rod_Blk,
            Process_2_Rod_Blk_Lot_No,
            Process_2_Rod_Blk_Tesla_1_Average_Data,
            Process_2_Rod_Blk_Tesla_2_Average_Data,
            Process_2_Rod_Blk_Tesla_3_Average_Data,
            Process_2_Rod_Blk_Tesla_4_Average_Data,
            Process_2_Rod_Blk_Tesla_1_Minimum_Data,
            Process_2_Rod_Blk_Tesla_2_Minimum_Data,
            Process_2_Rod_Blk_Tesla_3_Minimum_Data,
            Process_2_Rod_Blk_Tesla_4_Minimum_Data,
            Process_2_Rod_Blk_Tesla_1_Maximum_Data,
            Process_2_Rod_Blk_Tesla_2_Maximum_Data,
            Process_2_Rod_Blk_Tesla_3_Maximum_Data,
            Process_2_Rod_Blk_Tesla_4_Maximum_Data,
            Process_2_Rod_Blk_Inspection_1_Average_Data,
            Process_2_Rod_Blk_Inspection_2_Average_Data,
            Process_2_Rod_Blk_Inspection_3_Average_Data,
            Process_2_Rod_Blk_Inspection_4_Average_Data,
            Process_2_Rod_Blk_Inspection_5_Average_Data,
            Process_2_Rod_Blk_Inspection_6_Average_Data,
            Process_2_Rod_Blk_Inspection_7_Average_Data,
            Process_2_Rod_Blk_Inspection_8_Average_Data,
            Process_2_Rod_Blk_Inspection_9_Average_Data,
            Process_2_Rod_Blk_Inspection_1_Minimum_Data,
            Process_2_Rod_Blk_Inspection_2_Minimum_Data,
            Process_2_Rod_Blk_Inspection_3_Minimum_Data,
            Process_2_Rod_Blk_Inspection_4_Minimum_Data,
            Process_2_Rod_Blk_Inspection_5_Minimum_Data,
            Process_2_Rod_Blk_Inspection_6_Minimum_Data,
            Process_2_Rod_Blk_Inspection_7_Minimum_Data,
            Process_2_Rod_Blk_Inspection_8_Minimum_Data,
            Process_2_Rod_Blk_Inspection_9_Minimum_Data,
            Process_2_Rod_Blk_Inspection_1_Maximum_Data,
            Process_2_Rod_Blk_Inspection_2_Maximum_Data,
            Process_2_Rod_Blk_Inspection_3_Maximum_Data,
            Process_2_Rod_Blk_Inspection_4_Maximum_Data,
            Process_2_Rod_Blk_Inspection_5_Maximum_Data,
            Process_2_Rod_Blk_Inspection_6_Maximum_Data,
            Process_2_Rod_Blk_Inspection_7_Maximum_Data,
            Process_2_Rod_Blk_Inspection_8_Maximum_Data,
            Process_2_Rod_Blk_Inspection_9_Maximum_Data,
            Process_2_Df_Blk,
            Process_2_Df_Blk_Lot_No,
            Process_2_Df_Blk_Inspection_1_Average_Data,
            Process_2_Df_Blk_Inspection_2_Average_Data,
            Process_2_Df_Blk_Inspection_3_Average_Data,
            Process_2_Df_Blk_Inspection_4_Average_Data,
            Process_2_Df_Blk_Inspection_1_Minimum_Data,
            Process_2_Df_Blk_Inspection_2_Minimum_Data,
            Process_2_Df_Blk_Inspection_3_Minimum_Data,
            Process_2_Df_Blk_Inspection_4_Minimum_Data,
            Process_2_Df_Blk_Inspection_1_Maximum_Data,
            Process_2_Df_Blk_Inspection_2_Maximum_Data,
            Process_2_Df_Blk_Inspection_3_Maximum_Data,
            Process_2_Df_Blk_Inspection_4_Maximum_Data,
            Process_2_Df_Blk_Tensile_Rate_Of_Change_Average,
            Process_2_Df_Blk_Tensile_Rate_Of_Change_Minimum,
            Process_2_Df_Blk_Tensile_Rate_Of_Change_Maximum,
            Process_2_Df_Blk_Tensile_Start_Force_Average,
            Process_2_Df_Blk_Tensile_Start_Force_Minimum,
            Process_2_Df_Blk_Tensile_Start_Force_Maximum,
            Process_2_Df_Blk_Tensile_Terminating_Force_Average,
            Process_2_Df_Blk_Tensile_Terminating_Force_Minimum,
            Process_2_Df_Blk_Tensile_Terminating_Force_Maximum,
            Process_2_Df_Ring,
            Process_2_Df_Ring_Lot_No,
            Process_2_Washer,
            Process_2_Washer_Lot_No,
            Process_2_Lock_Nut,
            Process_2_Lock_Nut_Lot_No,
            Process_2_ST,
            Process_2_Actual_Time,
            Process_2_NG_Cause,
            Process_2_Repaired_Action,
            Process_3_S_N,
            Process_3_ID,
            Process_3_NAME,
            Process_3_Frame_Gasket,
            Process_3_Frame_Gasket_Lot_No,
            Process_3_Casing_Block,
            Process_3_Casing_Block_Lot_No,
            Process_3_Casing_Block_Inspection_1_Average_Data,
            Process_3_Casing_Block_Inspection_1_Minimum_Data,
            Process_3_Casing_Block_Inspection_1_Maximum_Data,
            Process_3_Casing_Gasket,
            Process_3_Casing_Gasket_Lot_No,
            Process_3_M4x16_Screw_1,
            Process_3_M4x16_Screw_1_Lot_No,
            Process_3_M4x16_Screw_2,
            Process_3_M4x16_Screw_2_Lot_No,
            Process_3_Ball_Cushion,
            Process_3_Ball_Cushion_Lot_No,
            Process_3_Frame_Cover,
            Process_3_Frame_Cover_Lot_No,
            Process_3_Partition_Board,
            Process_3_Partition_Board_Lot_No,
            Process_3_Built_In_Tube_1,
            Process_3_Built_In_Tube_1_Lot_No,
            Process_3_Built_In_Tube_2,
            Process_3_Built_In_Tube_2_Lot_No,
            Process_3_Head_Cover,
            Process_3_Head_Cover_Lot_No,
            Process_3_Casing_Packing,
            Process_3_Casing_Packing_Lot_No,
            Process_3_M4x12_Screw,
            Process_3_M4x12_Screw_Lot_No,
            Process_3_Csb_L,
            Process_3_Csb_L_Lot_No,
            Process_3_Csb_R,
            Process_3_Csb_R_Lot_No,
            Process_3_Head_Packing,
            Process_3_Head_Packing_Lot_No,
            Process_3_ST,
            Process_3_Actual_Time,
            Process_3_NG_Cause,
            Process_3_Repaired_Action,
            Process_4_S_N,
            Process_4_ID,
            Process_4_NAME,
            Process_4_Tank,
            Process_4_Tank_Lot_No,
            Process_4_Upper_Housing,
            Process_4_Upper_Housing_Lot_No,
            Process_4_Cord_Hook,
            Process_4_Cord_Hook_Lot_No,
            Process_4_M4x16_Screw,
            Process_4_M4x16_Screw_Lot_No,
            Process_4_Tank_Gasket,
            Process_4_Tank_Gasket_Lot_No,
            Process_4_Tank_Cover,
            Process_4_Tank_Cover_Lot_No,
            Process_4_Housing_Gasket,
            Process_4_Housing_Gasket_Lot_No,
            Process_4_M4x40_Screw,
            Process_4_M4x40_Screw_Lot_No,
            Process_4_PartitionGasket,
            Process_4_PartitionGasket_Lot_No,
            Process_4_M4x12_Screw,
            Process_4_M4x12_Screw_Lot_No,
            Process_4_Muffler,
            Process_4_Muffler_Lot_No,
            Process_4_Muffler_Gasket,
            Process_4_Muffler_Gasket_Lot_No,
            Process_4_VCR,
            Process_4_VCR_Lot_No,
            Process_4_ST,
            Process_4_Actual_Time,
            Process_4_NG_Cause,
            Process_4_Repaired_Action,
            Process_5_S_N,
            Process_5_ID,
            Process_5_NAME,
            Process_5_Rating_Label,
            Process_5_Rating_Label_Lot_No,
            Process_5_ST,
            Process_5_Actual_Time,
            Process_5_NG_Cause,
            Process_5_Repaired_Action,
            Process_6_S_N,
            Process_6_ID,
            Process_6_NAME,
            Process_6_Vinyl,
            Process_6_Vinyl_Lot_No,
            Process_6_ST,
            Process_6_Actual_Time,
            Process_6_NG_Cause,
            Process_6_Repaired_Action,
            Process_1_SERIAL_NO,
            Process_2_SERIAL_NO,
            Process_3_SERIAL_NO,
            Process_4_SERIAL_NO,
            Process_5_SERIAL_NO,
            Process_6_SERIAL_NO
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s
        )
    """
    
    # Execute the insert only for new records
    create_cursor.executemany(insert_query, new_records)
    mariadb_connection.commit()
    print(f"Successfully inserted {len(new_records)} new records into inspection_machine_data table")

def SelectAllDataFromTable(tableName):
    global create_cursor

    sqlStatement = f"SELECT * FROM {tableName}"
    create_cursor.execute(sqlStatement)
    myresult = create_cursor.fetchall()

    # Get column names from cursor description
    columns = [desc[0] for desc in create_cursor.description]
    
    # Create DataFrame
    df = pd.DataFrame(myresult, columns=columns)

    return df

def SelectSpecificDataFromTable(tableName, columnName):
    global create_cursor

    sqlStatement = f"SELECT * FROM {tableName} WHERE {columnName} = 'CARL'"
    create_cursor.execute(sqlStatement)
    myresult = create_cursor.fetchall()
    print(myresult)

def CloseConnection():
    global mariadb_connection

    mariadb_connection.close()
    
