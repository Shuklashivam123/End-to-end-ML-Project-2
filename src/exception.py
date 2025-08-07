import sys # Jo exception aayega vo sys module ke pass rahega
import logging
from src.logger import logging


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # here exc_tb used to give info kis jagah kis line me error aaya hai

    file_name=exc_tb.tb_frame.f_code.co_filename  # To get filename
    error_message="Error Occured in python script name [{0}] line number [{1}] error message [{2}] ".format(
        file_name,exc_tb.tb_lineno,str(error) )

    return error_message
   


class CustomException(Exception):  # Own custom exception class
    def __init__(self,error_message,error_detail:sys): # This is my constructor
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self): # When we raise custom exception this will return error message
        return self.error_message
    

if __name__=="__main__":

    try:
        1/0
    except Exception as e:
        logging.info("Divide by Zero Error!")
        raise CustomException(e,sys)