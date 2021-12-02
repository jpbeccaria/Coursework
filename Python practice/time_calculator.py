# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:41:26 2021

@author: Juan
"""



def add_time(start, duration, day = None):
    
    from datetime import datetime, timedelta

    # start = "11:00 AM"
    if day:
        if day == 'Monday' or day == 'monday':
            start_time = datetime.strptime(start, '%I:%M %p')
        elif day == 'Tuesday' or day == 'tuesday':
            start_time = datetime.strptime(start, '%I:%M %p')
            cambio_dia = timedelta(days = 1)
            start_time += cambio_dia
        elif day == 'Wednesday' or day == 'wednesday':
            start_time = datetime.strptime(start, '%I:%M %p')
            cambio_dia = timedelta(days = 2)
            start_time += cambio_dia
        elif day == 'Thuesday' or day == 'thuesday':
            start_time = datetime.strptime(start, '%I:%M %p')
            cambio_dia = timedelta(days = 3)
            start_time += cambio_dia
        elif day == 'Friday' or day == 'friday':
            start_time = datetime.strptime(start, '%I:%M %p')
            cambio_dia = timedelta(days = 4)
            start_time += cambio_dia
        elif day == 'Saturday' or day == 'saturday' or day == 'SaturDay' or day == 'saturDay':
            start_time = datetime.strptime(start, '%I:%M %p')
            cambio_dia = timedelta(days = 5)
            start_time += cambio_dia
        elif day == 'Sunday' or day == 'Sunday':
            start_time = datetime.strptime(start, '%I:%M %p')
            cambio_dia = timedelta(days = 6)
            start_time += cambio_dia
            
    else:
        start_time = datetime.strptime(start, '%I:%M %p')


    ##### duration
    dur = duration.split(':')
    if int(dur[0]) >= 24:
        days = int(dur[0]) // 24     #no deberia ser dias, sino lo que de de delta + las horas de ese dia
        hours = (int(dur[0]) / 24 - int(dur[0]) // 24) *24
        minutes = int(dur[1])
        delta = timedelta(days = days, hours = hours, minutes = minutes)
    else:
        delta_temp = datetime.strptime(duration, '%H:%M')
        delta= timedelta(hours=delta_temp.hour, minutes=delta_temp.minute)
    
    final = start_time + delta
    # new_time = final.strftime('%I:%M %p')
    
    # if day:
    #     read_day = datetime.strptime(day, '%A')
    #     final_day = read_day + delta 
    #     fday_str = final_day.strftime('%A')
    
    
    if final.day - start_time.day == 1:
        if day:
            new_time = final.strftime('%-I:%M %p, %A')
            result = new_time + " (next day)"
            return result
            
        else:
            new_time = final.strftime('%-I:%M %p')
            result = new_time + " (next day)"
            return result
    
    elif final.day == start_time.day:
        if day:
            new_time = final.strftime('%-I:%M %p, %A')
            result = new_time
            return result
            
        else:
            new_time = final.strftime('%-I:%M %p')
            result = new_time
            return result
        
    else:
        if day:
            new_time = final.strftime('%-I:%M %p, %A')
            days = final.day - start_time.day
            result = new_time + f" ({days} days later)"
            return result
            
        else:
            new_time = final.strftime('%-I:%M %p')
            days = final.day - start_time.day
            result = new_time + f" ({days} days later)"
            return result
        
        
        
    
        






holis = add_time("2:59 AM", "24:00", "saturDay")

# anda mal la parte de " '%-I:%M %p, %A' " aca no le gusta el "-" antes de la I pero me lo pedia la puta pagina de submision!