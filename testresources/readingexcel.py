from page_object_model.testresources import constants
from page_object_model.testresources.readingData import XLSReader
import xlrd


def getcelldata(testcasename, path):
    datalist = []
    xls = XLSReader(path)


    teststartrowindex = 0
    max_rows_in_sheet = xls.getRowCount(constants.DATASHEET)
    #print(testcasename)
    while not(xls.getCellData(constants.DATASHEET,teststartrowindex,0)==testcasename):
        teststartrowindex +=1


    colstartrowindex = teststartrowindex + 1
    datastartrowindex = colstartrowindex + 1
    maxrow = 0

    try:
        while (datastartrowindex+maxrow < max_rows_in_sheet and
               not xls.checkemptycell(constants.DATASHEET,datastartrowindex+maxrow,0)):
            maxrow += 1
        #print(maxrow)
    except Exception as e:
        pass

    maxcol = 0
    try:
        max_cols_in_sheet = xls.getColumnCount(constants.DATASHEET)
        row_to_check_for_max_col = colstartrowindex

        current_col = 0
        while(current_col < max_cols_in_sheet and
            not xls.checkemptycell(constants.DATASHEET,row_to_check_for_max_col,current_col)):
          maxcol = current_col
          current_col += 1
        #print(current_col)
    except Exception as e:
        pass

    for rNum in range(datastartrowindex, datastartrowindex+maxrow):
        datadictionary = {}
        for cNum in range(0, maxcol+1):
            datakey = xls.getCellData(constants.DATASHEET,colstartrowindex,cNum)
            datavalue = xls.getCellData(constants.DATASHEET,rNum,cNum)
            #print(datakey+":"+datavalue)
            datadictionary[datakey] = datavalue
        #print(datadictionary)
        datalist.append(datadictionary)
    return datalist

def isRunnable(testcasename, path):
    xls = XLSReader(path)
    rows = xls.getRowCount(constants.TESTSHEET)
    #print(rows)
    for rNum in range(0,rows):
        tname = xls.getCellDatabyColName(constants.TESTSHEET,rNum, constants.TCID)
        #print(tname)
        if tname==testcasename:
            runmode = xls.getCellDatabyColName(constants.TESTSHEET,rNum,constants.RUNMODE)
            #print(runmode)
            if(runmode==constants.RUNMODE_Y):
                return True
            else:
                return False







