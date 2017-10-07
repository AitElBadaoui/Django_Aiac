from django import template
import calendar
from datetime import date, timedelta

register = template.Library()

@register.filter(name='diviser')

def diviser(value, arg):
    try:
         i =(int(value)/int(arg))*100
         return round(i,2)
    except (ValueError, ZeroDivisionError):
        return None


@register.filter
def month_name(month_number):
    calendar.month_name[month_number]
    if  calendar.month_name[month_number] == "January":
        return "Janvier"
    elif calendar.month_name[month_number] == "February":
        return "Février"
    if calendar.month_name[month_number] == "March":
        return "Mars"
    elif calendar.month_name[month_number] == "April":
        return "Avril"

    if calendar.month_name[month_number] == "May":
        return "Mai"
    elif calendar.month_name[month_number] == "June":
        return "Juin"

    if calendar.month_name[month_number] == "July":
        return "Juillet"
    elif calendar.month_name[month_number] == "August":
        return "Août"

    if calendar.month_name[month_number] == "September":
        return "Septembre"
    elif calendar.month_name[month_number] == "October":
        return "Octobre"

    if calendar.month_name[month_number] == "November":
        return "Novembre"
    elif calendar.month_name[month_number] == "December":
        return "Décembre"

@register.filter
def H(value):
    if value == 1:
        return "3H30"
    elif value == 2:
        return "7H"
    else:
        return " "
@register.filter
def filter_heure(value):
    a = int(value)
    b = value - a

    if b == 0:
        return str(a) + "Heures"
    else:
        return str(a) + "H" + "30"

@register.filter
def level(value):
    if value =="S1" or value =="S2":
        return "1ERE ANNÉE " + str(value)
    elif value == "S3" or value== "S4":
        return "2EME ANNÉE " + str(value)
    else:
        return "3EME ANNÉE " + str(value)

