import os
import json
import pandas as pd
import requests
import statistics
import datetime
import timedelta
from requests.exceptions import HTTPError
from datetime import datetime as dt
from datetime import timedelta as td

def get_iata_airport_code():
  """
    Helps user find the relevant IATA 3-letter code for the airport they are attempting to search for 

    Parameters
    -----------
    Function will prompt user for an airport name and will display 10 entries of any airport name, airport country, airport codes that match the user's input 
    User will be prompted to select an option from the list of ten or re-type in a new entry.
    Function will then print out the name of the selected airport, country and airport code.
    Can return an empty list
    --------
    Examples
    ---------
    >>> get_iata_airport_code()
    Please enter name of airport > SIng
    The following entries (max 10) have been found:
      1 Fitzroy Crossing Australia FIZ
      2 Singerbhil India IXA
      3 Mersing Malaysia MEP
      4 Singapore Changi Singapore SIN
      5 Singleton Australia SIX
      6 Kapuskasing Canada YYU
      7 Robert Atty Bessing Airport Indonesia LNU
      8 Chicago Lansing Municipal Airport United States QQI
    Choose the entry (1-10) you want or 0 to re-enter > 4
    Singapore Changi
    Singapore
    SIN
  """
  def get_code(s):
  
    count=0
    answer=[]

    flightlabs_api_key = os.getenv("FLIGHTLABS_API_KEY")
    data=requests.get("https://app.goflightlabs.com/airports?access_key="+flightlabs_api_key+"&search="+s)

    # api will return False for 'success' key if string not found in its DB
    if isinstance(data.json(), dict):
      if data.json().get('success')==False: return answer

    # if found, data.json() returns a list of dicts
    for d in data.json():
      airport_name=d['airport_name']
      country_name=d['country_name']
      iata_code=d['iata_code']

      # takes care of wierd return values from api
      if airport_name is None: airport_name='None'
      else: airport_name=airport_name.strip()
      if country_name is None: country_name='None'
      else: country_name=country_name.strip()
      if iata_code is None: iata_code='None'
      else: iata_code=iata_code.strip()

      #returns a list of tuple triplets
      answer.append((airport_name,country_name,iata_code))
      count+=1
      if count>=10: break #max 10 entries in return list

    return answer

  airport_name=''
  airport_country=''
  airport_code=''

  # loop forever until we get the proper return, i.e., only 1 entry is returned
  while(True):
    s=input("Please enter name of airport > ")
    l=get_code(s) # returns a list of tuple triplets

    if (len(l)==1):
      airport_name=l[0][0]
      airport_country=l[0][1]
      airport_code=l[0][2]
      break
    if (len(l)==0): print("Not found! Please re-enter")
    else:
      print("The following entries (max 10) have been found:")
      for i, data in enumerate(l): print("   ", i+1, data[0], data[1], data[2])
      n=input("Choose the entry (1-10) you want or 0 to re-enter > ")
      if n in ['1','2','3','4','5','6','7','8','9','10']:
        if int(n)>len(l): continue #out of range, skip
        airport_name=l[int(n)-1][0]
        airport_country=l[int(n)-1][1]
        airport_code=l[int(n)-1][2]
        break

  print(airport_name)
  print(airport_country)
  print(airport_code)

def get_iata_airline_code():
  """
    Helps user find the relevant IATA 2-letter code for the airline they are attempting to search for 

    Parameters
    -----------
    Function will prompt user for an airline name and will display 10 entries of any airline name, country, airline codes that match the user's input 
    User will be prompted to select an option from the list of ten or re-type in a new entry.
    Function will then print out the name of the selected airline, country and airline code.
    Can return an empty list
    --------
    Examples
    ---------
    >>> get_iata_airline_code()
    Please enter name of airline > Sing
    The following entries (max 10) have been found:
      1 SIA Cargo Singapore SQ
      2 Jetstar Asia Airways - Singapore Singapore 3K
      3 World Air Leasing - Gambia United States 1W*
      4 Advance Leasing Company United States 4G*
      5 Advance Leasing Company United States BC*
      6 Airline Container Leasing United States JG*
      7 Tradewinds Airlines (Singapore) Singapore MI
      8 Malaysia-Singapore Airlines Mauritius ML
      9 MSA - Malaysia-Singapore Airlines Singapore ML
      10 Malaysian-Singapore Airlines Malaysia / Singapore ML
    Choose the entry (1-10) you want or 0 to re-enter > 2
    Jetstar Asia Airways - Singapore
    Singapore
    3K

  """
  def get_code(s):
    count=0
    answer=[]
  
    flightlabs_api_key = os.getenv("FLIGHTLABS_API_KEY")
    data=requests.get("https://app.goflightlabs.com/airlines?access_key="+flightlabs_api_key+"&search="+s)

    # api will return False for 'success' key if string not found in its DB
    if isinstance(data.json(), dict):
      if data.json().get('success')==False: return answer

    # if found, data.json() returns a list of dicts
    for d in data.json():
      airline_name=d['airline_name']
      country_name=d['country_name']
      iata_code=d['iata_code']

      # takes care of wierd return values from api
      if airline_name is None: airline_name='None'
      else: airline_name=airline_name.strip()
      if country_name is None: country_name='None'
      else: country_name=country_name.strip()
      if iata_code is None: iata_code='None'
      else: iata_code=iata_code.strip()

      #returns a list of tuple triplets
      answer.append((airline_name,country_name,iata_code))
      count+=1
      if count>=10: break #max 10 entries in return list

    return answer
  airline_name=''
  airline_country=''
  airline_code=''

  # loop forever until we get the proper return, i.e., only 1 entry is returned
  while(True):
    s=input("Please enter name of airline > ")
    l=get_code(s) # returns a list of tuple triplets

    if (len(l)==1):
      airline_name=l[0][0]
      airline_country=l[0][1]
      airline_code=l[0][2]
      break
    if (len(l)==0): print("Not found! Please re-enter")
    else:
      print("The following entries (max 10) have been found:")
      for i, data in enumerate(l): print("   ", i+1, data[0], data[1], data[2])
      n=input("Choose the entry (1-10) you want or 0 to re-enter > ")
      if n in ['1','2','3','4','5','6','7','8','9','10']:
        if int(n)>len(l): continue #out of range, skip
        airline_name=l[int(n)-1][0]
        airline_country=l[int(n)-1][1]
        airline_code=l[int(n)-1][2]
        break

  print(airline_name)
  print(airline_country)
  print(airline_code)

def flight_delay(airport='FRA',airline='SQ',flight_number='26'):
  """
    Finds the average 14-day delay over the past 2 weeks for any scheduled flight to any airport

    Parameters
    -----------
    arrival_airport: 3-letter IATA code of arrival airport of desired flight 
    airline: 2-letter IATA airline code
    flight_number: Flight number of scheduled flight
    
    Returns a dataframe with the start date and end date of the search, relevant flight number, departure and arrival airports and the average delay in minutes over the time frame of the search.
    Default set to flight SQ26, departing Singapore and arriving Frankfurt. 
    --------
    Examples
    ---------
    >>> flight_delay(arrival_airport='NRT',airline='SQ',flight_number='12')
        Start Date    End Date Flight number Departure Airport Arrival Airport  \
    0  2022-11-23  2022-12-07          SQ12               SIN             NRT   

      Average Delay (Mins)  
    0              0.066667  

  """
  api_key = os.getenv("AVIATION_EDGE_API_KEY")
  
  # Parse strings in city_input_list 
  
  #error handling for arrival airport code
  if not isinstance(airport, str): raise Exception("Airport code must contain only strings")
  if len(airport)!=3: raise Exception("Error in input: please enter 3-letter IATA airport code")
  
  #error handling for airline code
  if not isinstance(airline, str): raise Exception("Airline code must contain only strings")
  if len(airline)!=2: raise Exception("Error in input: please enter 2-letter IATA airline code")
  
  #error handling for flight no
  try:
    flight_number = int(flight_number)
  except ValueError:
    print('Please input a valid flight number')

  #getting start and end dates
  today = dt.now()
  three_days = td(days=4)
  fourteen_days = td(days=14)
  end_date = today - three_days
  start_date = end_date - fourteen_days
  end_date_str = str(end_date).split(" ")[0]
  start_date_str = str(start_date).split(" ")[0]
    
  #api call
  params = {'key':api_key, 'code':airport, 'type':'arrival', 'date_from':start_date_str, 'date_to':end_date_str, 'airline_iata':airline, 'flight_number':flight_number}
  try:
    r = requests.get('https://aviation-edge.com/v2/public/flightsHistory', params = params)
    r.raise_for_status() # If the response was successful, no Exception will be raised
  except HTTPError as http_err:
      print(f'HTTP error occurred: {http_err}')
  except Exception as err: 
      print(f'Other error occurred: {err}')

  delay=[]
  delay_minutes=[]
  dep_airport=[]

  f=r.json() #f is now a dict object
  
  for d in f:
    for k in d:
      if k == 'arrival': #obtains delay by subtracting scheduled arrival time from estimated arrival time, returns delay in minutes
        delay.append(0 if ((datetime.datetime.strptime((" ".join(d['arrival']['estimatedTime'].split("t"))), '%Y-%m-%d %H:%M:%S.%f'))-(datetime.datetime.strptime((" ".join(d['arrival']['scheduledTime'].split("t"))), '%Y-%m-%d %H:%M:%S.%f'))).days<0 else ((datetime.datetime.strptime((" ".join(d['arrival']['estimatedTime'].split("t"))), '%Y-%m-%d %H:%M:%S.%f'))-(datetime.datetime.strptime((" ".join(d['arrival']['scheduledTime'].split("t"))), '%Y-%m-%d %H:%M:%S.%f'))).seconds)
      if k == 'departure':
        dep_airport.append(d['departure']['iataCode'].upper())
  for i in delay:
    delay_minutes.append(int(i/60))
  
  airline_flight_number = ''.join(airline+str(flight_number))
  average = sum(delay_minutes) / len(delay_minutes)
  average_list = [average]
  start_date_list = [start_date_str]
  end_date_list = [end_date_str]
  flight_no_list = [airline_flight_number]
  arr_airport_list = [''.join(airport)]
  z = zip(start_date_list, end_date_list, flight_no_list, dep_airport[:2], arr_airport_list, average_list)

  df=pd.DataFrame(z, columns=['Start Date', 'End Date', 'Flight number', 'Departure Airport', 'Arrival Airport', 'Average Delay (Mins)'])
  
  return(df)

def get_flights(airport='SIN', date_from='2022-01-03', date_to='2022-01-30',airline='UA',flight_number='1'):
  """
    Finds historical scheduled flight details for any user-inputted flight over a user-defined time-frame to any user-defined airport

    Parameters
    -----------
    airport: 3-letter IATA code of arrival airport of desired flight 
    date_from: Start date of the search timeframe
    date_to: End date of the search timeframe (can be the same as date_from to search only 1 flight), must be within 31 days of date_from and 3 days before current date
    airline: 2-letter IATA airline code
    flight_number: Flight number of scheduled flight
    
    Returns a dataframe with the start date and end date of the search, relevant flight number, departure and arrival airports and the average delay in minutes over the time frame of the search.
    Default set to flight UA1, departing San Francisco and arriving Singapore from 3 Jan to 30 Jan 2022. 
    --------
    Examples
    ---------
    >>> get_flights(airport='FRA', date_from='2022-09-03', date_to='2022-09-05',airline='SQ',flight_number='26')
        Departure date Flight number Departure airport Scheduled departure time  \
      0     2022-09-02          sq26               sin             23:55:00.000   
      1     2022-09-03          sq26               sin             23:55:00.000   
      2     2022-09-04          sq26               sin             23:55:00.000   

        Actual departure time Arrival airport Arrival date Scheduled arrival time  \
      0          00:45:00.000             fra   2022-09-03           06:45:00.000   
      1          01:01:00.000             fra   2022-09-04           06:45:00.000   
      2          00:27:00.000             fra   2022-09-05           06:45:00.000   

        Actual arrival time  Delay in minutes  
      0        06:42:00.000               0.0  
      1        07:09:00.000              24.0  
      2        06:52:00.000               7.0  

  """
  api_key = os.getenv("AVIATION_EDGE_API_KEY")
  # Parse strings in city_input_list 
  
  #error handling for arrival airport code
  if not isinstance(airport, str): raise Exception("Airport code must contain only strings")
  if len(airport)!=3: raise Exception("Error in input: please enter 3-letter IATA airport code")

  #error handling for date from 
  try:
    datetime.datetime.strptime(date_from, '%Y-%m-%d')
  except ValueError:
    print('Please input date in YYYY-MM-DD format')
  
  #error handling for date to
  try:
    datetime.datetime.strptime(date_to, '%Y-%m-%d')
  except ValueError:
    print('Please input date in YYYY-MM-DD format')
  
  #error handling for airline code
  if not isinstance(airline, str): raise Exception("Airline code must contain only strings")
  if len(airline)!=2: raise Exception("Error in input: please enter 2-letter IATA airline code")
  
  #error handling for flight no
  try:
    flight_number = int(flight_number)
  except ValueError:
    print('Please input a valid flight number')

  # Proceed to GET requests
  dep_date=[]
  arr_date=[]
  flight_no=[]
  dep_airport=[]
  arr_airport=[]
  sch_dep_time=[]
  actual_dep_time=[]
  sch_arr_time=[]
  actual_arr_time=[]
  delay=[]

  params = {'key':api_key, 'code':airport, 'type':'arrival', 'date_from':date_from, 'date_to':date_to, 'airline_iata':airline, 'flight_number':flight_number}
  try:
      r = requests.get('https://aviation-edge.com/v2/public/flightsHistory', params = params)
      r.raise_for_status() # If the response was successful, no Exception will be raised
  except HTTPError as http_err:
      print(f'HTTP error occurred: {http_err}')
  except Exception as err: 
      print(f'Other error occurred: {err}')

  f=r.json() #f is now a dict object
  for d in f:
    for k in d:
      if k == 'flight':
        flight_no.append(d['flight']['iataNumber'])
      if k == 'departure':
        dep_airport.append(d['departure']['iataCode'])
        dep_date.append((d['departure']['scheduledTime'].split("t"))[0])
        sch_dep_time.append((d['departure']['scheduledTime'].split("t"))[1])
        actual_dep_time.append((d['departure']['actualTime'].split("t"))[1])
      if k == 'arrival':
        arr_airport.append(d['arrival']['iataCode'])
        sch_arr_time.append((d['arrival']['scheduledTime'].split("t"))[1])
        arr_date.append((d['arrival']['scheduledTime'].split("t"))[0])
        actual_arr_time.append((d['arrival']['estimatedTime'].split("t"))[1]) #some actual time missing
        delay.append(0 if ((datetime.datetime.strptime((" ".join(d['arrival']['estimatedTime'].split("t"))), '%Y-%m-%d %H:%M:%S.%f'))-(datetime.datetime.strptime((" ".join(d['arrival']['scheduledTime'].split("t"))), '%Y-%m-%d %H:%M:%S.%f'))).days<0 else ((((datetime.datetime.strptime((" ".join(d['arrival']['estimatedTime'].split("t"))), '%Y-%m-%d %H:%M:%S.%f'))-(datetime.datetime.strptime((" ".join(d['arrival']['scheduledTime'].split("t"))), '%Y-%m-%d %H:%M:%S.%f'))).seconds)/60))

  z=list(zip(dep_date, flight_no, dep_airport, sch_dep_time, actual_dep_time, arr_airport, arr_date, sch_arr_time, actual_arr_time, delay))
  df=pd.DataFrame(z, columns=['Departure date','Flight number','Departure airport','Scheduled departure time', 'Actual departure time','Arrival airport','Arrival date','Scheduled arrival time','Actual arrival time', 'Delay in minutes'])
  return(df)
