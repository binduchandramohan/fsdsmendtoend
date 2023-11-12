import sys

class customexception(Exception):
    def __init__(self,error_message,error_details:sys):
        # we need the script name where error occurs
        # the line number where it errors
        # actual error message
        self.error_message = error_message
        #self.error_details = error_details.exec_info()
        #exc_tb is execution trace back
        _,_,exc_tb = error_details.exc_info()
        self.line_no =  exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name,self.line_no,str(self.error_message))
    
if __name__ == "__main__":
    try:

        a = 1/0 
    except Exception as e:
        raise customexception(e,sys)
# execute in terminal using --> python src/DimondPricePrediction/exception.py 