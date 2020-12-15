class Date:
    
    # Set the constructors for the type date
    def __init__ (self,d,m,y):
        self.day = int(d)
        self.month = int(m)
        self.year = int(y)

        
           
    # Accessor Methods
    def getDay(self):
        return self.day
    def getMonth(self):
        return self.month
    def getYear(self):
        return self.year
    


    def accurateDate(self):   ##method to check if the date provided is accurate
        try:
            if self.day<=0 or self.day>31:  ##the day must be between 0 and 31 
                return False
            if self.month>12 or self.month<=0:   ##the month must be between 0 to 12
                return False
        except ValueError:
            return ("Error found")
        
    
        
    
    ##a method to check if the month occured in a leap  year
    def leap_year(self):
        if self.month%4==0 or self.year%400==0 and self.year%100 ==0:
            if self.day ==29:  #if it is a leap year then febuarary ends on the 29
                self.month=3   ##the month changes to the first date of the next month
                self.day=1
            else:
                self.day+=1 ##if its any other day, add one to the day 
        else:
            if self.day==28:   ##if its not a leap year, then the month ends on the 28
                self.month=3   ##increment the month by 1 and 
                self.day=1     ## the day is reset to 1
            else:
                self.day+=1   ##the day increases by 1 if its any other day then the 28

    ## a method to determine the next day of the current day
    def Next(self):
        if self.month == 2:   ##checks if month is febuary is it a leap year
            self.leap_year()
            
        ## if it Jan, March, May, July, Aug, Oct, the month ends on the 31st
        elif self.month==(1 or 3 or 5 or 7 or 8 or 10): 
            if self.day ==31: ##reset the date to the first month of the next month if the date is 31
                self.month+=1
                self.day=1
            else:
                self.day+=1  ##add 1 if its any other day
        
        elif self.month==12:  ##if the month is december, then reset the date to the first day of the next year
            if self.day ==31: 
                self.month=1
                self.day=1
                self.year+=1
            else:
                self.day+=1  ##any other day in Dec, add one to the day

        else:  ##if its any other month then, the last day of the month is 30
            if self.day==30:
                self.day=1   ##change the date to the first of the next month after the 30th
                self.month+=1
            else:
                self.day+=1  ##increase the day by one if its any other day 
        
        ##return the day, month and the year
        return self.day,self.month,self.year
    
    ##a method to determine the day before today
    def Prev (self):
        if self.month == 3:  ##if the month is march check its a a leap year
            if self.day==1 and self.month%4==0 or self.year%400==0 and self.year%100 ==0:
                self.day=29    ## set the date to the 29 of Feb 
                self.month==2
            else:
                self.day -=1  ##if any other day decrease the day by 1
        ##check if the month is feb, april, June, Sept, Nov
        elif self.month ==(2 or 4 or 6 or 9 or 11):  
            if self.day==1:  ##if the day is 1 the previous day would be 31st of the previous month
                self.day=31
                self.month-=1
            else:
                self.day+= 1  ##if any other day decrease by 1
        elif self.month==1:  ##check if the month is Jan 
            if self.day==1: ##set the day to the 31st of December 
                self.day=31
                self.month=12
                self.year-=1
            else:
                self.day-=1  ##decrease the day by 1 
                
        else: ##if its any other month 
            if self.day==1: ##the initial day is 1 then the day before occurs is the 30th of the previous month
                self.day=30
                self.month-=1
            else:
                self.day-=1  ##if its another day decrease the day by 1
        return self.day,self.month,self.year
    
    ##used to return a new object with the same month,day and year 
    def copy(self):
        new_date=Date(self.day,self.month,self.year)
        return new_date
    
    ## a method to determine if the second date provided it before the first date
    def isBefore(self,d):
        if d.year<self.year or d.month<self.month or d.day<self.day:
            return True  ##outputs true if the statement is correct
        else:
            return False
        
    ## a method to determine if the second date provided it after the first date   
    def isAfter (self,d):
        if d.year>self.year or d.month>self.month or d.day>self.day:
            return True  ##outputs true if the statement is correct
        else:
            return False
        
    ##checks if the second date provided is the same as the first date
    def isEqual (self,d):
        if d.year==self.year and d.month==self.month and d.day==self.day:
            return True  ##output true if the statement is correct
        else:
            return False
        
    ## a method to add a number of days to the current date
    def add_Days(self,d): 
        for i in range (0,d):  ## a for loop that iterates the number of days added
            d,m,y = self.Next()   ##find the next day
        return (d,m,y)  ##exit the loop once all the iterations are done 
    
    ## a method to find the days inbetween two dates provided
    def days_Between(self,d):
        count=0 ##initialize a variable to 0
        dcopy =self.copy() ##use the copy method from earlier to copy the date to another variable
        if dcopy.isEqual(d)== True:
            count=0  
        elif dcopy.isAfter(d) ==True:  ##check if the date is after and if so use the next day method and increment until the date is not after anymore
            while dcopy.isAfter(d) ==True:
                dcopy.Next() 
                count+=1 
        elif dcopy.isBefore(d) == True:   ##if the second date is before the first date interate the while loop until the date is not before
            while dcopy.isBefore(d) ==True: 
                dcopy.Prev()   ##use the previous day method to keep decreasing the date by 1
                count+=1 
        return count  
        
        
##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def represent(date): ##represent the date in a specific way
    ## change the date to a string, remove the spaces and  replace every comma with a forwardslash
    stringDate= (str(date)).replace(',','/').replace(" ", "") 
    return stringDate  ##output the string 

def dateConverter():   ##a function is used to test the different aspects of the function
    date= '1/1/1999'
    d,m,y= date.split('/')
    date2= '1/1/1999'
    d2,m2,y2= date2.split('/')
    ny = Date(d,m,y)
    d = Date(d2,m2,y2)
    number=5
    
    return (date,date2, ny,d,number)
    
def main():
    counter=1
    date,date2, ny,d,number=dateConverter()
    print("The date is",date)
    
    ##exception handling call to determine if the dates are accurate
    value=ny.accurateDate()
    ##check if the try and except statements have been checked
    if value == False:
        print("error in the dates provided")  ##print error message
    ##if there are no errors
    else:
        while counter!=8: ## a loop iteration to print all the following methods with the original dates
            date,date2, ny,d,number=dateConverter()  ##call the main function

            if counter==1:
                print("The date tomorrow is",represent(ny.Next()))
            elif counter==2:
                print("The date of yesturday is", represent(ny.Prev()))
            elif counter==3:
                print("The date",date,"is before",date2,":",ny.isBefore(d))
            elif counter==4:
                print("The date",date,"is after",date2,":",ny.isAfter(d))
            elif counter==5:
                print("The date",date,"is equal",date2,":",ny.isEqual(d))
            elif counter==6:
                print("The date after",number,"days:",represent(ny.add_Days(number)))
            elif counter==7:
                print("The number of days between",date,"and",date2,"is:",ny.days_Between(d))
            counter+=1
        
main()
