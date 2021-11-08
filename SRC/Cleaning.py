import re

def date (x):

    """
    THIS FUNCTION WILL HELP ME TO CLEAN 'Date' COLUMN. 
    FOR EVERYTHING RELATED TO THE YEAR... RETURNS THE YYYY
    """
    dicc_year = {  
        '2021' : '2021',
        '2020' : '2020',
        '2019' : '2019',
        '2018' : '2018',
        '2017' : '2017',
        '2016' : '2016',
        '2015' : '2015',
        '2014' : '2014',
        '2013' : '2013',
        '2012' : '2012',
        '2011' : '2011',
        '2010' : '2010'}

    for key,values in dicc_year.items():

        if re.match(values, x):
            return key 
        
    return "Unknown" 


def clean_year(new_column="Date",column_name="Date Joined"):

    unicorn["Date"] = unicorn["Date Joined"].str[-4:]
