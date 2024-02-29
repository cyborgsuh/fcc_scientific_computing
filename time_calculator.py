class time_calculator:
    def __init__(self,Start_time,End_time,Start_day=None):
        self.Start_time_list=Start_time.split(":")
        self.Start_time_list[1]=(self.Start_time_list[1].split(" "))[0]
        self.Start_time_MI=Start_time[-2:]
        self.End_time_list=End_time.split(":")
        self.Start_hour=int(self.Start_time_list[0])
        self.Start_minute=int(self.Start_time_list[1])
        self.End_time_list=End_time.split(":")
        self.End_hour=int(self.End_time_list[0])
        self.End_minute=int(self.End_time_list[1])
        self.condition_hour=self.Start_hour+self.End_hour
        self.condition_minute=self.Start_minute+self.End_minute
        self.days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        self.Start_day=Start_day
        self.final_hour,self.final_minute=None,None
        self.n_days=None

    def c12(self,c_h):

        if c_h>=12:
            count_hour=0
            while c_h>12:
                count_hour+=1
                c_h-=1
            if self.Start_time_MI=='AM':
                self.Start_time_MI='PM'
            elif self.Start_time_MI=='PM':
                self.Start_time_MI='AM'
            
        else:
            count_hour=c_h
            
        if count_hour==0:
            count_hour=12 

        return count_hour
    
    def c60(self,c_m):
        
        if c_m>60:
            count_minute=0
            self.condition_hour+=1
            while c_m>60:
                count_minute+=1
                c_m-=1
        else:
            count_minute=c_m

        return count_minute
            
    def c2400(self,c_h):
        
        if c_h>24:
            rem=c_h%24
            if rem==0:
                return 1
            else:
                return rem
            
    def c_nextday(self):

        if self.Start_day!=None:
            self.Start_day=self.Start_day.lower()
            if self.condition_hour<12:
                return self.Start_day
            elif self.condition_hour>=12 and self.condition_hour<24 and self.Start_time_MI=='PM':
                return f'{self.days[(self.days.index(self.Start_day))+1]}'
            elif self.condition_hour>=24 and self.Start_time_MI=='PM':
                rem_days=self.condition_hour/24
                rem_days=rem_days.__ceil__()
                start=self.days.index(self.Start_day)
                restart=len(self.days)
                for i in range(rem_days):
                    start+=1
                    if start==restart:
                        start=0
                if rem_days==0 or rem_days==1:
                    return f'{self.days[start]} (next day)'
                else:
                    return f'{self.days[start]} ({rem_days} days later)'
            elif self.condition_hour>=24 and self.Start_time_MI=='AM':
                rem_days=self.condition_hour/24
                rem_days=rem_days.__floor__()
                start=self.days.index(self.Start_day)
                restart=len(self.days)
                for i in range(rem_days):
                    start+=1
                    if start==restart:
                        start=0
                if rem_days==0 or rem_days==1:
                    return f'{self.days[start]} (next day)'
                else:
                    return f'{self.days[start]} ({rem_days} days later)'
        elif self.Start_day==None:
            if self.condition_hour>=12 and self.condition_hour<24 and self.Start_time_MI=='PM':
                return '(next day)'
            elif self.condition_hour>=24 and self.Start_time_MI=='PM':
                rem_days=self.condition_hour//24
                rem_days+=1
                if rem_days==1:
                    return '(next day)'
                elif rem_days!=0:
                    return f'({rem_days} days later)'
                else:
                    return None
            elif self.condition_hour>=24 and self.Start_time_MI=='AM':
                rem_days=self.condition_hour//24
                if rem_days==1:
                    return '(next day)'
                elif rem_days!=0:
                    return f'({rem_days} days later)'
                else:
                    return None
            else:
                return None
            

    def calculate_time(self):
        
        if self.condition_hour<24:
            self.final_minute=time_calculator.c60(self,self.condition_minute)
            self.n_days=self.c_nextday()
            self.final_hour=time_calculator.c12(self,self.condition_hour)
        elif self.condition_hour>=24:
            self.final_minute=time_calculator.c60(self,self.condition_minute)
            self.n_days=self.c_nextday()
            self.final_hour=time_calculator.c2400(self,self.condition_hour)
            self.final_hour=time_calculator.c12(self,self.final_hour)
        
    def show(self):
        time_calculator.calculate_time(self)
        if self.n_days==None:
            return(f'{self.final_hour}:{self.final_minute:02d} {self.Start_time_MI}')

        else:
            if self.n_days.split()[0] in self.days:
                return(f'{self.final_hour}:{self.final_minute:02d} {self.Start_time_MI}, {self.n_days.capitalize()}')
            else:
                return(f'{self.final_hour}:{self.final_minute:02d} {self.Start_time_MI} {self.n_days.capitalize()}')

if __name__=="__main__":

    calculate=time_calculator("3:30 PM", "2:12", "Monday")
    final_time=calculate.show()
    print(final_time)

    