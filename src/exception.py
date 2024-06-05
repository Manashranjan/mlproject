import sys # this module provide functions and variables that are used to manipulate different parts of python run time environment
import logging

def error_message_details(error,error_detail:sys):
    __,__,exc_tb=error_detail.exc_info() # the error details will be stored in the exc_tb obj from exc_info
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = "Errror occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
     
     
    )
    return error_message
    
    # The above function will be called by the following class

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
    
