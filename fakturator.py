from datetime import datetime, timedelta
import calendar

class Fakturator():
    def __init__(self):
        self.today = datetime.today()

    def __year_of_previous_month(self):
        if (self.today.month == 1):
            return self.today.year-1
        return self.today.year

    def __previous_month(self):
        if (self.today.month == 1):
            return 12
        return self.today.month-1

    def __last_day_of_previous_month(self):
        if (self.today.month == 1):
            return calendar.monthrange(self.today.year-1,self.__previous_month())[1]
        return calendar.monthrange(self.today.year,self.__previous_month())[1]
    
    def get_invoice_no(self):
        return self.today.strftime("%m-%Y")
    
    def get_today(self):
        return self.today.strftime("%d.%m.%Y")
    
    def get_deadline_date(self,deadline_days=15):
        return (self.today+timedelta(days=deadline_days)).strftime("%d.%m.%Y")

    def get_date_from(self):
        return "{}.{}.{}".format(1,self.__previous_month(), self.__year_of_previous_month())

    def get_date_to(self):
      return "{}.{}.{}".format(self.__last_day_of_previous_month(),self.__previous_month(), self.__year_of_previous_month())