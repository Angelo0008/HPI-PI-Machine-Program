# %%
from Imports import *
import DateAndTimeManager
import Sql

isProgramRunning = True
isCompiling = True

isDebugMode = False
isAutoMode = False

#Csv Data
allPIData = ""
piData = ""
previousPiData = ""
tempPiData = ""
process5Data = ""
tempProcess5Data = ""

#Read Checker
isPiDataReaded = False
isProcess5DataReaded = False

#Date
dateToday = "2024/11/04"
dateTodayDashFormat = "2024-11-04"
calendarPicker = ""

#Output
csvData = ""
compiledData = ""

#Row To Read
piRow = 0
process5Row = 0

isCanProceed = True

#Process Type
isMasterPump = False
is60FCXP001P = False
isTrial = False
isTrialRunning = False
isRunning = False
isNG = False
isGood = False
isNGPressure = False
isNGFlow = False

readCount = 0

# %%
def settingFC1Directory():
    global isDebugMode

    if isDebugMode:
        return r'\\192.168.2.19\general\INSPECTION-MACHINE\FC1\Debug\log000_FC1.csv'
    else:
        return r'\\192.168.2.19\general\INSPECTION-MACHINE\FC1\log000_FC1.csv'

# %%
def settingProcess5Directory():
    global isDebugMode

    if isDebugMode:
        return fr'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT5\log000_5.csv'
    else:
        return fr'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT5\log000_5.csv'

# %%
def ReadPIMachine():
    global isDebugMode

    global dateToday
    global dateTodayDashFormat

    global allPIData
    global piData

    global previousPiData

    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)

    # piDirectory = (r'\\192.168.2.19\ai_team\AI Program\Outputs\CompiledPiMachine')
    # os.chdir(piDirectory)
    
    # #Appending Latest Data Into List
    # allPIData = pd.read_csv('CompiledPIMachine.csv', encoding='latin1')
    
    # piData = allPIData[(allPIData["DATE"].isin([dateToday]))]

    Sql.SqlConnection()

    allPIData = Sql.SelectAllDataFromTable("inspection_machine_data")
    piData = allPIData[(allPIData["DATE"].astype(str).isin([dateTodayDashFormat]))]

    # print(piData["TIME"].values[0].replace("0 days ", ""))

    # tempPiData = piData.iloc[[piRow], :]

    # return str(tempPiData["TIME"].values[0])
    # return str(tempPiData.iloc[0, 2])

# ReadPIMachine()

# %%
# ReadPIMachine()
# allPIData

# %%
# previousPiDirectory = (r'\\192.168.2.19\general\INSPECTION-MACHINE\FC1\FC1 Data')
# os.chdir(previousPiDirectory)
# #Reading All FC1 Previous Data
# previousPiData = glob.glob('*.csv')
# previousPiDataList = []

# %%
# previousPiData

# %%
# #Appending All Previous Data Into List
# for f in previousPiData:
#     a = pd.read_csv(f, encoding='latin1', skiprows=1)
#     previousPiDataList.append(a)

# # previousPiDataList.reverse()


# if isDebugMode:
#     piDirectory = (r'\\192.168.2.19\general\INSPECTION-MACHINE\FC1\Debug')
# else:
#     piDirectory = (r'\\192.168.2.19\general\INSPECTION-MACHINE\FC1')
    
# os.chdir(piDirectory)

# #Appending Latest Data Into List
# allPIData = pd.read_csv('log000_FC1.csv', encoding='latin1', skiprows=1)
# previousPiDataList.append(allPIData)





# allPIData = pd.concat(previousPiDataList, ignore_index=True)

# %%

# previousPiDataList[0]
# # allPIData

# %%
def ReadProcess5():
    global isDebugMode

    global dateToday

    global process5Data

    if isDebugMode:
        process5Directory = (r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT5\Debug')
    else:
        process5Directory = (r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT5')

    # os.chdir(process5Directory)

    # process5Data = pd.read_csv(f'log000_5.csv', encoding='latin1')
    # process5Data = process5Data[(process5Data["DATE"].isin([dateToday]))]

    Sql.SqlConnection()

    process5Data = Sql.SelectAllDataFromTable("process5_data")
    process5Data = process5Data[(process5Data["Process_5_DATE"].isin([dateToday]))]


# %%
def checkIfCanProceed():
    global isCompiling

    global allPIData
    global piData
    global tempPiData
    global process5Data
    global tempProcess5Data

    global piRow
    global process5Row

    global isCanProceed

    global isMasterPump
    global is60FCXP001P
    global isTrial
    global isTrialRunning
    global isRunning
    global isNG
    global isGood
    global isNGPressure
    global isNGFlow

    #Private Variables
    isPiDataBlank = True
    isProcess5DataBlank = True

    #Reseting Value
    isCanProceed = False

    isMasterPump = False
    is60FCXP001P = False
    isTrial = False
    isTrialRunning = False
    isRunning = False
    isNG = False
    isGood = False
    isNGPressure = False
    isNGFlow = False

    try:
        tempPiData = piData.iloc[[piRow], :]
        isPiDataBlank = False
        print("Pi Not Blank")
    except:
        isPiDataBlank = True
        isCanProceed = False
        isCompiling = False
        print("Pi Data Blank")
    try:
        tempProcess5Data = process5Data.iloc[[process5Row], :]
        tempProcess5Data["Process_5_NG_Cause"]
        if tempProcess5Data["Process_5_NG_Cause"].values[0].replace(' ', '') == "NGPRESSURE":
            isNGPressure = True
            isCanProceed = True
            print("NG Pressure")
    except:
        pass
    try:
        tempProcess5Data = process5Data.iloc[[process5Row], :]
        tempProcess5Data["Process_5_NG_Cause"]
        if tempProcess5Data["Process_5_NG_Cause"].values[0].replace(' ', '') == "NGFLOW":
            isNGFlow = True
            isCanProceed = True
            print("NG Flow")
    except:
        pass

    if not isPiDataBlank and not isNGPressure and not isNGFlow:
        if "M" in tempPiData["MODEL_CODE"].values[0]:
            isMasterPump = True
            isCanProceed = True
            print("Master Pump")

        elif "60FCXP001P" in tempPiData["MODEL_CODE"].values[0]:
            is60FCXP001P = True
            isCanProceed = True
            print("60FCXP001P")

        #Checking If Trial/TrialRunning
        elif len(str(tempPiData["S_N"].values[0])) < 9:
            print("Checking If Trial/TrialRunning")

            piDataFilteredGood = allPIData[(allPIData["PASS_NG"].isin([1])) & (allPIData["MODEL_CODE"].isin([tempPiData["MODEL_CODE"].values[0]]))]
            serialNumberList = piDataFilteredGood["S_N"].values

            sameSerialList = []
            for a in serialNumberList:
            #Checking S/N If Same Value Exists = Running
                if tempPiData["S_N"].values == a:
                    sameSerialList.append(a)
                if len(sameSerialList) > 5:
                    print("Trial Running")
                    isTrialRunning = True
                    isCanProceed = True
            print(f"Same Value Length is {len(sameSerialList)}")
            if not isTrialRunning:
                print("Trial")

                isTrial = True
                isCanProceed = True

        #Checking If NG/Running
        elif tempPiData["PASS_NG"].values == "0":
            print("Checking If NG/Running")

            piDataFilteredGood = allPIData[(allPIData["PASS_NG"].isin([1])) & (allPIData["MODEL_CODE"].isin([tempPiData["MODEL_CODE"].values[0]]))]
            serialNumberList = piDataFilteredGood["S_N"].values

            sameSerialList = []
            for a in serialNumberList:
            #Checking S/N If Same Value Exists = Running
                if tempPiData["S_N"].values == a:
                    sameSerialList.append(a)
                if len(sameSerialList) > 2:
                    print("Running")
                    isRunning = True
                    isCanProceed = True

            if not isRunning:
                print("NG")

                try:
                    tempProcess5Data = process5Data.iloc[[process5Row], :]
                    print("Process 5 Not Blank")
                    isNG = True
                    isCanProceed = True
                except:
                    isCanProceed = False
                    isCompiling = False
                    print("Process 5 Data Blank")

        #Checking If Good/Running
        elif tempPiData["PASS_NG"].values == "1":
            print("Checking If Good/Running")

            piDataFilteredGood = allPIData[(allPIData["PASS_NG"].isin([1])) & (allPIData["MODEL_CODE"].isin([tempPiData["MODEL_CODE"].values[0]]))]
            #Not Including the tempPiData
            # piDataFilteredGood = piDataFilteredGood[(piDataFilteredGood["TIME"].isin([tempPiData["TIME"].values[0]]))]
            serialNumberList = piDataFilteredGood["S_N"].values


            sameSerialList = []
            for a in serialNumberList:
            #Checking S/N If Same Value Exists = Running
                if tempPiData["S_N"].values == a:
                    sameSerialList.append(a)
                if len(sameSerialList) > 2:
                    print("Running")
                    isRunning = True
                    isCanProceed = True
            
            if not isRunning:
                print("Good")

                try:
                    tempProcess5Data = process5Data.iloc[[process5Row], :]
                    print("Process 5 Not Blank")
                    isGood = True
                    isCanProceed = True
                except:
                    isCanProceed = False
                    isCompiling = False
                    print("Process 5 Data Blank")

        else:
            isCanProceed = False
            isCompiling = False
            print("Reached The Last Row")

# %%
def compileCsv():
    global piData
    global tempPiData
    global process5Data
    global tempProcess5Data

    global piRow
    global process5Row

    global csvData
    global compiledData

    global isMasterPump
    global isTrial
    global isTrialRunning
    global isRunning
    global isNG
    global isGood
    global isNGPressure
    global isNGFlow
  
    csvData = {
        "DATE": [tempPiData["DATE"].values[0]],
        "TIME": [str(tempPiData.iloc[0, 2]).replace("0 days ", "")],
        "MODEL CODE": [tempPiData["MODEL_CODE"].values[0]],
        "PROCESS S/N": "",
        "S/N": [tempPiData["S_N"].values[0]],
        "PASS/NG": [tempPiData["PASS_NG"].values[0]],
        "VOLTAGE MAX (V)": [tempPiData["VOLTAGE_MAX_V"].values[0]],
        "WATTAGE MAX (W)": [tempPiData["WATTAGE_MAX_W"].values[0]],
        "CLOSED PRESSURE_MAX (kPa)": [tempPiData["CLOSED_PRESSURE_MAX_kPa"].values[0]],
        "VOLTAGE Middle (V)": [tempPiData["VOLTAGE_Middle_V"].values[0]],
        "WATTAGE Middle (W)": [tempPiData["WATTAGE_Middle_W"].values[0]],
        "AMPERAGE Middle (A)": [tempPiData["AMPERAGE_Middle_A"].values[0]],
        "CLOSED PRESSURE Middle (kPa)": [tempPiData["CLOSED_PRESSURE_Middle_kPa"].values[0]],
        "VOLTAGE MIN (V)": [tempPiData["VOLTAGE_MIN_V"].values[0]],
        "WATTAGE MIN (W)": [tempPiData["WATTAGE_MIN_W"].values[0]],
        "CLOSED PRESSURE MIN (kPa)": [tempPiData["CLOSED_PRESSURE_MIN_kPa"].values[0]]
    }
    csvData = pd.DataFrame(csvData)

    print(piRow)
    
    if isMasterPump:
        print("Master Pump")
        csvData["PROCESS S/N"] = "MASTER PUMP"   
        piRow += 1
        compiledData = pd.concat([compiledData, csvData], ignore_index=True)
    elif is60FCXP001P:
        print("60FCXP001P")
        csvData["PROCESS S/N"] = "INSPECTION ONLY"
        piRow += 1
        compiledData = pd.concat([compiledData, csvData], ignore_index=True)
    elif isTrial:
        print("Trial")
        csvData["PROCESS S/N"] = "TRIAL"   
        piRow += 1
        compiledData = pd.concat([compiledData, csvData], ignore_index=True)
    elif isTrialRunning:
        print("Trial Running")
        csvData["PROCESS S/N"] = "TRIAL RUNNING"   
        piRow += 1
        compiledData = pd.concat([compiledData, csvData], ignore_index=True)
    elif isRunning:
        print("Running")
        csvData["PROCESS S/N"] = "RUNNING"   
        piRow += 1
        compiledData = pd.concat([compiledData, csvData], ignore_index=True)
    elif isNG:
        print("NG")
        csvData["PROCESS S/N"] = tempProcess5Data["Process_5_S_N"].values[0]
        piRow += 1
        process5Row += 1
        compiledData = pd.concat([compiledData, csvData], ignore_index=True)
    elif isGood:
        print("Good")
        csvData["PROCESS S/N"] = tempProcess5Data["Process_5_S_N"].values[0]
        piRow += 1
        process5Row += 1
        compiledData = pd.concat([compiledData, csvData], ignore_index=True)
    elif isNGPressure:
        print("NG PRESSURE")
        csvData["DATE"] = "NG PRESSURE" 
        csvData["TIME"] = "NG PRESSURE" 
        csvData["MODEL CODE"] = "NG PRESSURE" 
        csvData["PROCESS S/N"] = tempProcess5Data["Process_5_S_N"].values[0]
        csvData["S/N"] = "NG PRESSURE" 
        csvData["PASS/NG"] = "NG PRESSURE" 
        csvData["VOLTAGE MAX (V)"] = "NG PRESSURE" 
        csvData["WATTAGE MAX (W)"] = "NG PRESSURE" 
        csvData["CLOSED PRESSURE_MAX (kPa)"] = "NG PRESSURE" 
        csvData["VOLTAGE Middle (V)"] = "NG PRESSURE" 
        csvData["WATTAGE Middle (W)"] = "NG PRESSURE" 
        csvData["AMPERAGE Middle (A)"] = "NG PRESSURE" 
        csvData["CLOSED PRESSURE Middle (kPa)"] = "NG PRESSURE" 
        csvData["dB(A) 1"] = "NG PRESSURE" 
        csvData["dB(A) 2"] = "NG PRESSURE" 
        csvData["dB(A) 3"] = "NG PRESSURE" 
        csvData["VOLTAGE MIN (V)"] = "NG PRESSURE" 
        csvData["WATTAGE MIN (W)"] = "NG PRESSURE" 
        csvData["CLOSED PRESSURE MIN (kPa)"] = "NG PRESSURE" 
        csvData["CHECKING"] = "NG PRESSURE" 
        process5Row += 1
        compiledData = pd.concat([compiledData, csvData], ignore_index=True)
    elif isNGFlow:
        print("NG FLOW")
        csvData["DATE"] = "NG FLOW" 
        csvData["TIME"] = "NG FLOW" 
        csvData["MODEL CODE"] = "NG FLOW" 
        csvData["PROCESS S/N"] = tempProcess5Data["Process_5_S_N"].values[0]
        csvData["S/N"] = "NG FLOW" 
        csvData["PASS/NG"] = "NG FLOW" 
        csvData["VOLTAGE MAX (V)"] = "NG FLOW" 
        csvData["WATTAGE MAX (W)"] = "NG FLOW" 
        csvData["CLOSED PRESSURE_MAX (kPa)"] = "NG FLOW" 
        csvData["VOLTAGE Middle (V)"] = "NG FLOW" 
        csvData["WATTAGE Middle (W)"] = "NG FLOW" 
        csvData["AMPERAGE Middle (A)"] = "NG FLOW" 
        csvData["CLOSED PRESSURE Middle (kPa)"] = "NG FLOW" 
        csvData["dB(A) 1"] = "NG FLOW" 
        csvData["dB(A) 2"] = "NG FLOW" 
        csvData["dB(A) 3"] = "NG FLOW" 
        csvData["VOLTAGE MIN (V)"] = "NG FLOW" 
        csvData["WATTAGE MIN (W)"] = "NG FLOW" 
        csvData["CLOSED PRESSURE MIN (kPa)"] = "NG FLOW" 
        csvData["CHECKING"] = "NG FLOW" 
        process5Row += 1
        compiledData = pd.concat([compiledData, csvData], ignore_index=True)

# %%
def WriteCsv(excelData):
    global isDebugMode

    global dateToday

    if isDebugMode:
        fileDirectory = (r'\\192.168.2.19\ai_team\AI Program\Outputs\Debug\PICompiled')
    else:
        fileDirectory = (r'\\192.168.2.19\ai_team\AI Program\Outputs\PICompiled')

    os.chdir(fileDirectory)
    print(os.getcwd())
    
    print("Creating New File")
    #Create Excel File
    newValue = pd.concat([excelData], axis = 0, ignore_index = True)
    wireFrame = newValue
    wireFrame.to_csv(f"PICompiled{dateToday.replace('/', '-')}.csv", index = False)

# %%
def startCompiler():
    global isCompiling

    global csvData
    global compiledData 

    global piRow
    global process5Row

    global isPiDataReaded
    global isProcess5DataReaded

    global isCanProceed

    #Reset Variables
    isCompiling = True
    piRow = 0
    process5Row = 0
    
    col = [
        "DATE",
        "TIME",
        "MODEL CODE",
        "PROCESS S/N",
        "S/N",
        "PASS/NG",
        "VOLTAGE MAX (V)",
        "WATTAGE MAX (W)",
        "CLOSED PRESSURE_MAX (kPa)",
        "VOLTAGE Middle (V)",
        "WATTAGE Middle (W)",
        "AMPERAGE Middle (A)",
        "CLOSED PRESSURE Middle (kPa)",
        "dB(A) 1",
        "dB(A) 2",
        "dB(A) 3",
        "VOLTAGE MIN (V)",
        "WATTAGE MIN (W)",
        "CLOSED PRESSURE MIN (kPa)",
        "CHECKING"
    ]
    compiledData = pd.DataFrame(columns=col)

    ReadPIMachine()
    while True:
        try:
            ReadProcess5()
            break
        except:
            pass

    while isCompiling:
        # DateAndTimeManager.GetDateToday()

        # while not isPiDataReaded:
        #     try:
        #         ReadPIMachine()
        #         isPiDataReaded = True
        #     except:
        #         pass
        # isPiDataReaded = False

        checkIfCanProceed()
        if isCanProceed:
            compileCsv()
    WriteCsv(compiledData)

    time.sleep(1)

# %%
def startProgram():
    global isProgramRunning
    global isDebugMode
    global isAutoMode
    
    global isPiDataReaded
    global isProcess5DataReaded

    global dateToday

    global readCount


    # DateAndTimeManager.GetDateToday()
    # dateToday = DateAndTimeManager.dateToday

    #Checking Changes In CSV File Every Seconds
    #Reading Original File
    piDataOrig = os.path.getmtime(settingFC1Directory())
    process5DataOrig = os.path.getmtime(settingProcess5Directory())

    updateDate()
    while isProgramRunning:
        print(dateToday)
        if isAutoMode:
            DateAndTimeManager.GetDateToday()
            if dateToday != DateAndTimeManager.dateToday:
                DateAndTimeManager.GetDateToday()
                dateToday = DateAndTimeManager.dateToday

        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while not isPiDataReaded:
            try:
                piDataCurrent = os.path.getmtime(settingFC1Directory())
                isPiDataReaded = True
            except:
                print("Failed Reading Of PiCompiled Trying Again In 1 Seconds")
                pass
        isPiDataReaded = False

        while not isProcess5DataReaded:
            try:
                process5DataCurrent = os.path.getmtime(settingProcess5Directory())
                isProcess5DataReaded = True
            except:
                print("Failed Reading Of PiCompiled Trying Again In 1 Seconds")
                pass
        isProcess5DataReaded = False

        #If Changes Detected In File
        if piDataCurrent != piDataOrig or process5DataCurrent != process5DataOrig:
            print("Changes Detected")

            startCompiler()

            #Setting The Original File Onto Current File
            piDataOrig = piDataCurrent
            process5DataOrig = process5DataCurrent

        print("Waiting For Changes In PiCompiled")
        
        #Clearing Cmd Logs When Reaches 10 Lines
        readCount += 1
        if readCount >= 10:
            os.system('cls')
            readCount = 0
        time.sleep(1)
        #_______________________________________


# %%
#Call When Closing GUI Window
def StopProgram():
    global isProgramRunning

    isProgramRunning = False
    root.destroy()

# %%
def updateDate():
    global dateToday
    global dateTodayDashFormat
    global calendarPicker

    selectedDate = calendarPicker.get_date()
    selectedDateSlashFormat = selectedDate.strftime("%Y/%m/%d")
    selectedDateDashFormat = selectedDate.strftime("%Y-%m-%d")

    dateToday = selectedDateSlashFormat
    dateTodayDashFormat = selectedDateDashFormat

# %%
def updateDatePrompt():
    answer = askokcancel(title='Confirmation', message='Are you sure you want to change date?')
    if answer:
        updateDate()

# %%
applyButton = ""
autoModeButton = ""
calendarPicker = ""
compileButton = ""

def activateAutoMode():
    global applyButton
    global isAutoMode
    global autoModeButton
    global calendarPicker

    if not isAutoMode:
        isAutoMode = True
        applyButton.config(state= "disabled")
        calendarPicker.config(state= "disabled")
        compileButton.config(state= "disabled")
        autoModeButton.config(image = on)
    else:
        isAutoMode = False
        applyButton.config(state= "normal")
        calendarPicker.config(state= "normal")
        compileButton.config(state= "normal")
        autoModeButton.config(image = off)

# %%
#Creating GUI

#Fixing Blur
windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.title('Process 1')
root.geometry('800x400+50+50')
root.resizable(False, False)

on = PhotoImage(file= "Icons/on.png")
off = PhotoImage(file= "Icons/off.png")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

#Label
message = tk.Label(root, text="PI Machine Compiler", font=("Arial", 12, "bold"))
message.grid(column=0, row=1, columnspan=2)

calendarPicker = DateEntry(root, width=16, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy/mm/dd')
calendarPicker.grid(column=0, row=2, pady=20, padx=(200, 0))

#Button
applyButton = tk.Button(root, text='APPLY', font=("Arial", 9), command = updateDatePrompt, width=10, height=1)
applyButton.grid(column=1, row=2, padx=(0, 200))
applyButton.config(bg="lightgreen", fg="black")

autoModeLabel = tk.Label(root, text="Auto Mode", font=("Arial", 12, "bold"))
autoModeLabel.grid(column=0, row=3, padx=(150, 0))

autoModeButton = Button(root, image = off, bd=0, command=activateAutoMode)
autoModeButton.grid(column=1, row=3, padx=(0, 150))

#Button
compileButton = tk.Button(root, text='COMPILE', font=("Arial", 12), command = startCompiler, width=15, height=1)
compileButton.grid(column=0, row=4, pady=20, columnspan=2)
compileButton.config(bg="lightgreen", fg="black")

threading.Thread(target=startProgram).start()

root.protocol("WM_DELETE_WINDOW", StopProgram)
root.mainloop()




