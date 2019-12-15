# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:36:07 2019

@author: Cheng Cheng ANU

Australia public holiday generator
"""

# ACT public holidays
# https://www.legislation.act.gov.au/View/a/1958-19/current/PDF/1958-19.PDF
# New Year's Day: 1 Jan (if that day falls on a Saturday or Sunday, the day AND the following Monday)
# Australia Day: 26 Jan (if that day falls on a Saturday or Sunday, the following Monday)
# Canberra Day: 2nd Monday in March
# Good Friday: two days before Easter
# Easter Saturday: one day before Easter
# Easter Sunday
# Easter Monday: one day after Easter
# Anzac Day: 25 Apr (if that day falls on a Sunday, the following Monday)
# Reconciliation Day: 27 May (if that is not a Monday, the following Monday)
# Queen's Birthday: 2nd Monday in June
# Labour Day: 1st Monday in October
# Christmas Day: 25 Dec (if that day falls on a Saturday, the day AND the following Monday; if that day falls on a Sunday, the day AND the following Tuesday)
# Boxing Day: 26 Dec (if that day falls on a Saturday, the day AND the following Monday; if that day falls on a Sunday, the day AND the following Tuesday)

# NSW public holidays
# https://www.legislation.nsw.gov.au/#/view/act/2010/115/part2/sec4
# New Year's Day: 1 Jan (When 1 January is a Saturday or Sunday, there is to be an additional public holiday on the following Monday)
# Australia Day: 26 Jan (When 26 January is a Saturday or Sunday, there is to be no public holiday on that day and instead the following Monday is to be a public holiday)
# Good Friday: two days before Easter
# Easter Saturday: one day before Easter
# Easter Sunday
# Easter Monday: one day after Easter
# Anzac Day: 25 Apr
# Queen's Birthday: 2nd Monday in June
# Labour Day: 1st Monday in October
# Christmas Day: 25 Dec (When 25 December is a Saturday, there is to be an additional public holiday on the following Monday; When 25 December is a Sunday, there is to be an additional public holiday on the following Tuesday)
# Boxing Day: 26 Dec (When 26 December is a Saturday, there is to be an additional public holiday on the following Monday; When 26 December is a Sunday, there is to be an additional public holiday on the following Tuesday)

# NT public holidays
# https://legislation.nt.gov.au/api/sitecore/Act/PDF_History?id=21437
# New Year's Day: 1 Jan (if that day falls on a Saturday or Sunday, the day AND the following Monday)
# Australia Day: 26 Jan (if that day falls on a Saturday or Sunday, the following Monday)
# Good Friday: two days before Easter
# Easter Saturday: one day before Easter
# Easter Monday: one day after Easter
# Anzac Day: 25 Apr (or, if that day falls on a Sunday, the following Monday)
# May day: 1st Monday in May
# Queen's Birthday: 2nd Monday in June
# Picnic Day: 1st Monday in August
# Christmas Day: 25 Dec (and, if that day falls on a Saturday or Sunday, the following Monday)
# Boxing Day: 26 Dec (or, if that day falls on a Saturday, the following Monday or, if 26 December falls on a Sunday or Monday, the following Tuesday)

# QlD public holidays
# https://www.legislation.qld.gov.au/view/pdf/inforce/current/act-1983-018
# New Year's Day: 1 Jan (if that day falls on a Saturday or Sunday, the day AND the following Monday)
# Australia Day: 26 Jan (or, if that day falls on a Saturday or Sunday, the following Monday)
# Good Friday: two days before Easter
# Easter Saturday: one day before Easter
# Easter Sunday
# Easter Monday: one day after Easter
# Anzac Day: 25 Apr (or, if that day falls on a Sunday, the following Monday)
# Labour Day: 1st Monday in May
# Queen's Birthday: 1st Monday in October
# Christmas Day: 25 Dec (and, if that day falls on a Saturday, the following Monday; if that day falls on a Sunday, the following Tuesday)
# Boxing Day: 26 Dec (and, if that day falls on a Saturday, the following Monday; if that day falls on a Sunday, the following Tuesday)

# SA public holidays
# https://www.safework.sa.gov.au/law-compliance/laws-regulations/public-holidays?id=2483
# New Year's Day: 1 Jan (If a Saturday, normal rates apply and the following Monday is the public holiday. If a Sunday, that and the following Monday are both public holidays)
# Australia Day: 26 Jan (If a Saturday, normal rates apply and the following Monday is the public holiday. If a Sunday, that and the following Monday are both public holidays)
# Adelaide Cup Day: 2nd Monday in March (A proclamation is effective until 2020 - assumed to be continued)
# Good Friday: two days before Easter
# Easter Saturday: one day before Easter
# Easter Monday: one day after Easter
# Anzac Day: 25 Apr (If a Saturday, that day is the public holiday. If a Sunday, that and the following Monday are both public holidays)
# Queen's Birthday: 2nd Monday in June
# Labour Day: 1st Monday in October
# Christmas Day: 25 Dec (If a Saturday, normal rates apply and the following Monday is the public holiday. If a Sunday, that and the following Monday are both public holidays)
# Boxing Day/Proclamation Day: 26 Dec (If a Saturday, normal rates apply and the following Monday is the public holiday. If a Sunday or Monday, that and the following Tuesday are both public holidays)

# TAS public holidays
# https://www.legislation.tas.gov.au/view/html/inforce/current/act-2000-096#GS4@EN
# New Year's Day: 1 Jan (unless that day falls on a Saturday or Sunday, in which case the Monday following New Year's Day)
# Australia Day: 26 Jan (unless that day falls on a Saturday or Sunday, in which case the following Monday)
# Labour Day: 2nd Monday in March
# Good Friday: two days before Easter
# Easter Monday: one day after Easter
# Anzac Day: 25 Apr
# Queen's Birthday: 2nd Monday in June
# Christmas Day: 25 Dec (and, if that day falls on a Saturday, the following Monday; if that day falls on a Sunday, the following Tuesday)
# Boxing Day: 26 Dec (or, if that day falls on a Saturday, the following Monday; if that day falls on a Sunday, the following Tuesday)

# VIC public holidays
# http://www.legislation.vic.gov.au/domino/Web_Notes/LDMS/LTObject_Store/ltobjst10.nsf/DDE300B846EED9C7CA257616000A3571/A665FB533199C4D0CA2583630003FE5D/$FILE/93-119aa025%20authorised.pdf
# New Year's Day: 1 Jan (if that day falls on a Saturday or Sunday, the day AND the following Monday)
# Australia Day: 26 Jan (or, if that day falls on a Saturday or Sunday, the following Monday)
# Labour Day: 2nd Monday in March
# Good Friday: two days before Easter
# Easter Saturday: one day before Easter
# Easter Sunday
# Easter Monday: one day after Easter
# Anzac Day: 25 Apr
# Queen's Birthday: 2nd Monday in June
# Melbourne Cup Day: 1st Tuesday in November
# Christmas Day: 25 Dec (or, if that day falls on a Saturday, the following Monday; if that day falls on a Sunday, the following Tuesday)
# Boxing Day: 26 Dec (if that day falls on a Saturday, the day AND the following Monday; if that day falls on a Sunday, the day AND the following Tuesday)


# WA public holidays
# https://www.legislation.wa.gov.au/legislation/prod/filestore.nsf/FileURL/mrdoc_23507.pdf/$FILE/Public%20and%20Bank%20Holidays%20Act%201972%20-%20%5B02-e0-06%5D.pdf?OpenElement
# New Year's Day: 1 Jan (if that day falls on a Saturday or Sunday, the day AND the following Monday)
# Australia Day: 26 Jan (or, if that day falls on a Saturday or Sunday, the following Monday)
# Labour Day: 1st Monday in March
# Good Friday: two days before Easter
# Easter Monday: one day after Easter
# Anzac Day: 25 Apr (if that day falls on a Saturday or Sunday, the day AND the following Monday)
# Western Australia Dat: 1st Monday in June
# Queen's Birthday: end of September or start of October (Monday)
# Christmas Day: 25 Dec (if that day falls on a Saturday or Sunday, the day AND the following Monday)
# Boxing Day: 26 Dec (if that day falls on a Saturday, the day AND the following Monday; if that day falls on a Sunday or Monday, the day AND the following Tuesday)

years = [2019,2020]
state_list = ["ACT","NSW","NT","QLD","SA","TAS","VIC","WA"]

import datetime
import pandas as pd

def calc_easter(year):
    ''' Returns Easter as a date object. 
        http://code.activestate.com/recipes/576517-calculate-easter-western-given-a-year/ '''
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    return datetime.date(year, month, day)

def observation(d,c,i):
    ''' Return public holiday d and/or its observation.
        c = 0: if d falls on a Saturday or Sunday, the following Monday is observed.
        c = 1: if d falls on a Saturday, the following Monday is observed; if d falls on a Sunday, the following Tuesday is observed.
        c = 2: if d falls on a Saturday, the following Monday is observed; if d falls on a Sunday or Monday, the following Tuesday is observed.
        C = 3: if d falls on a Sunday, the following Monday is observed.
        i = 0: return d AND its observation; i = 1: return d OR its observation.
    '''
    if c == 1:
        # if d falls on a Saturday, return the following Monday; if d falls on a Sunday, return the following Tuesday.
        if d.weekday() == 5 or d.weekday() == 6:
            obs = d + datetime.timedelta(days = 2)
        else:
            obs = d
    elif c == 0:
        # if d falls on a Saturday or Sunday, return the following Monday.
        if d.weekday() == 5:
            obs = d + datetime.timedelta(days = 2)
        elif d.weekday() == 6:
            obs = d + datetime.timedelta(days = 1)
        else:
            obs = d
    elif c == 2:
        # if d falls on a Saturday, return the following Monday; if d falls on a Sunday or Monday, return the following Tuesday.
        if d.weekday() == 5 or d.weekday() == 6:
            obs = d + datetime.timedelta(days = 2)
        elif d.weekday() == 0:
            obs = d + datetime.timedelta(days = 1)
        else:
            obs = d
    elif c == 3:
        # if d falls on a Sunday, return the following Monday.
        if d.weekday() == 6:
            obs = d + datetime.timedelta(days = 1)
        else:
            obs = d
    if i == 0:
        return list(set([d,obs]))
    else:
        return [obs]

def nth_weekday(year,month,nth,wd):
    start_month = datetime.date(year,month,1)
    end_month = datetime.date(year,month+1,1) - datetime.timedelta(days = 1)
    appearance = 0
    next_day = start_month
    while appearance < nth:
        if next_day > end_month:
            break
        if next_day.weekday() == wd:
            appearance += 1
        next_day += datetime.timedelta(days = 1)
    return next_day - datetime.timedelta(days = 1)

result = pd.DataFrame(columns = ["Year","Month","Day","ACT","NSW","NT","QLD","SA","TAS","VIC","WA"])
for year in years:
    ph_dict = {}
    for state in state_list:
        if state == "ACT":
            ph = []
            # New Year
            ph.extend(observation(datetime.date(year,1,1),0,0))
            # Australia Day
            ph.extend(observation(datetime.date(year,1,26),0,1))
            # Canberra Day
            ph.append(nth_weekday(year,3,2,0))
            # Easter
            easter = calc_easter(year)
            ph.append(easter)
            ph.append(easter - datetime.timedelta(days = 2))
            ph.append(easter - datetime.timedelta(days = 1))
            ph.append(easter + datetime.timedelta(days = 1))
            # Anzac day
            ph.extend(observation(datetime.date(year,4,25),3,1))
            # Reconciliation Day
            rec_weekday = datetime.date(year,5,27).weekday()
            if rec_weekday != 0:
                rec_day = datetime.date(year,5,27) + datetime.timedelta(days = (7-rec_weekday))
            else:
                rec_day = datetime.date(year,5,27)
            ph.append(rec_day)
            # Queen's Birthday
            ph.append(nth_weekday(year,6,2,0))
            # Labour Day
            ph.append(nth_weekday(year,10,1,0))
            # Christmas
            ph.extend(observation(datetime.date(year,12,25),1,0))
            # Boxing day
            ph.extend(observation(datetime.date(year,12,26),1,0))
            ph_dict[state] = ph
        elif state == "NSW":
            ph = []
            # New Year
            ph.extend(observation(datetime.date(year,1,1),0,0))
            # Australia Day
            ph.extend(observation(datetime.date(year,1,26),0,1))
            # Easter
            easter = calc_easter(year)
            ph.append(easter)
            ph.append(easter - datetime.timedelta(days = 2))
            ph.append(easter - datetime.timedelta(days = 1))
            ph.append(easter + datetime.timedelta(days = 1))
            # Anzac day
            ph.append(datetime.date(year,4,25))
            # Queen's Birthday
            ph.append(nth_weekday(year,6,2,0))
            # Labour Day
            ph.append(nth_weekday(year,10,1,0))
            # Christmas
            ph.extend(observation(datetime.date(year,12,25),1,0))
            # Boxing day
            ph.extend(observation(datetime.date(year,12,26),1,0))
            ph_dict[state] = ph
        elif state == "NT":
            ph = []
            # New Year
            ph.extend(observation(datetime.date(year,1,1),0,0))
            # Australia Day
            ph.extend(observation(datetime.date(year,1,26),0,1))
            # Easter
            easter = calc_easter(year)
            ph.append(easter - datetime.timedelta(days = 2))
            ph.append(easter - datetime.timedelta(days = 1))
            ph.append(easter + datetime.timedelta(days = 1))
            # Anzac day
            ph.extend(observation(datetime.date(year,4,25),3,1))
            # May day
            ph.append(nth_weekday(year,5,1,0))
            # Queen's Birthday
            ph.append(nth_weekday(year,6,2,0))
            # Picnic Day
            ph.append(nth_weekday(year,8,1,0))
            # Christmas
            ph.extend(observation(datetime.date(year,12,25),0,0))
            # Boxing day
            ph.extend(observation(datetime.date(year,12,26),2,1))
            ph_dict[state] = ph
        elif state == "QLD":
            ph = []
            # New Year
            ph.extend(observation(datetime.date(year,1,1),0,0))
            # Australia Day
            ph.extend(observation(datetime.date(year,1,26),0,1))
            # Easter
            easter = calc_easter(year)
            ph.append(easter)
            ph.append(easter - datetime.timedelta(days = 2))
            ph.append(easter - datetime.timedelta(days = 1))
            ph.append(easter + datetime.timedelta(days = 1))
            # Anzac day
            ph.extend(observation(datetime.date(year,4,25),3,1))
            # Queen's Birthday
            ph.append(nth_weekday(year,10,1,0))
            # Labour Day
            ph.append(nth_weekday(year,5,1,0))
            # Christmas
            ph.extend(observation(datetime.date(year,12,25),1,0))
            # Boxing day
            ph.extend(observation(datetime.date(year,12,26),1,0))
            ph_dict[state] = ph
        elif state == "SA":
            ph = []
            # New Year
            new_year = datetime.date(year,1,1)
            if new_year.weekday() == 5:
                ph.append(new_year + datetime.timedelta(days = 2))
            elif new_year.weekday() == 6:
                ph.append(new_year)
                ph.append(new_year + datetime.timedelta(days = 1))
            else:
                ph.append(new_year)
            # Australia Day
            aus_day = datetime.date(year,1,26)
            if aus_day.weekday() == 5:
                ph.append(aus_day + datetime.timedelta(days = 2))
            elif aus_day.weekday() == 6:
                ph.append(aus_day)
                ph.append(aus_day + datetime.timedelta(days = 1))
            else:
                ph.append(aus_day)
            # Adelaide Cup Day
            ph.append(nth_weekday(year,3,2,0))
            # Easter
            easter = calc_easter(year)
            ph.append(easter - datetime.timedelta(days = 2))
            ph.append(easter - datetime.timedelta(days = 1))
            ph.append(easter + datetime.timedelta(days = 1))
            # Anzac day
            ph.extend(observation(datetime.date(year,4,25),3,0))
            # Queen's Birthday
            ph.append(nth_weekday(year,6,2,0))
            # Labour Day
            ph.append(nth_weekday(year,10,1,0))
            # Christmas
            chr = datetime.date(year,12,25)
            if chr.weekday() == 5:
                ph.append(chr + datetime.timedelta(days = 2))
            elif chr.weekday() == 6:
                ph.append(chr)
                ph.append(chr + datetime.timedelta(days = 1))
            else:
                ph.append(chr)
            # Boxing day
            box = datetime.date(year,12,26)
            if box.weekday() == 5:
                ph.append(box + datetime.timedelta(days = 2))
            elif box.weekday() == 6:
                ph.append(box)
                ph.append(box + datetime.timedelta(days = 2))
            elif box.weekday() == 0:
                ph.append(box)
                ph.append(box + datetime.timedelta(days = 1))
            else:
                ph.append(box)
            ph_dict[state] = ph
        elif state == "TAS":
            ph = []
            # New Year
            ph.extend(observation(datetime.date(year,1,1),0,1))
            # Australia Day
            ph.extend(observation(datetime.date(year,1,26),0,1))
            # Labour Day
            ph.append(nth_weekday(year,3,2,0))
            # Easter
            easter = calc_easter(year)
            ph.append(easter - datetime.timedelta(days = 2))
            ph.append(easter + datetime.timedelta(days = 1))
            # Anzac day
            ph.append(datetime.date(year,4,25))
            # Queen's Birthday
            ph.append(nth_weekday(year,6,2,0))
            # Christmas
            ph.extend(observation(datetime.date(year,12,25),1,0))
            # Boxing day
            ph.extend(observation(datetime.date(year,12,26),1,1))
            ph_dict[state] = ph
        elif state == "VIC":
            ph = []
            # New Year
            ph.extend(observation(datetime.date(year,1,1),0,0))
            # Australia Day
            ph.extend(observation(datetime.date(year,1,26),0,1))
            # Labour Day
            ph.append(nth_weekday(year,3,2,0))
            # Easter
            easter = calc_easter(year)
            ph.append(easter)
            ph.append(easter - datetime.timedelta(days = 2))
            ph.append(easter - datetime.timedelta(days = 1))
            ph.append(easter + datetime.timedelta(days = 1))
            # Anzac day
            ph.append(datetime.date(year,4,25))
            # Queen's Birthday
            ph.append(nth_weekday(year,6,2,0))
            # Melbourne Cup Day
            ph.append(nth_weekday(year,11,1,1))
            # Christmas
            ph.extend(observation(datetime.date(year,12,25),1,1))
            # Boxing day
            ph.extend(observation(datetime.date(year,12,26),1,0))
            ph_dict[state] = ph
        elif state == "WA":
            ph = []
            # New Year
            ph.extend(observation(datetime.date(year,1,1),0,0))
            # Australia Day
            ph.extend(observation(datetime.date(year,1,26),0,1))
            # Labour Day
            ph.append(nth_weekday(year,3,1,0))
            # Easter
            easter = calc_easter(year)
            ph.append(easter - datetime.timedelta(days = 2))
            ph.append(easter + datetime.timedelta(days = 1))
            # Anzac day
            ph.extend(observation(datetime.date(year,4,25),0,0))
            # Western Australia Day
            ph.append(nth_weekday(year,6,1,0))
            # Christmas
            ph.extend(observation(datetime.date(year,12,25),0,0))
            # Boxing day
            ph.extend(observation(datetime.date(year,12,26),2,0))
            # Queen's Birthday - assumed to be the Monday closest to 9/30
            test = datetime.date(year,9,30).weekday()
            if test <= 3:
                ph.append(datetime.date(year,9,30) - datetime.timedelta(days = test))
            else:
                ph.append(datetime.date(year,9,30) + datetime.timedelta(days = (7-test)))
            ph_dict[state] = ph
    begin_year = datetime.date(year,1,1)
    end_year = datetime.date(year,12,31)
    one_day = datetime.timedelta(days = 1)
    next_day = begin_year
    for day in range(0,366):
        if next_day > end_year:
            break
        month = next_day.month
        day = next_day.day
        id_list = []
        for state in state_list:
            if next_day in ph_dict[state]:
                id_list.append(0)
            else:
                id_list.append(1)
        result.loc[len(result)] = [year,month,day] + id_list
        next_day += one_day
        
result.to_csv("test.csv", index = False)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
