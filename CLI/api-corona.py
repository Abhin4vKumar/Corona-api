import requests
api="https://api.covid19api.com/summary"
data=dict()
def refresh_data():
    global data
    z = requests.request('GET',api)
    data = eval(z.text)
def display_data(data):
    print('Global Details')
    print('-'*40)
    decor(data['Global'])
    while True:
        z = input('Wanna Search country ? (Y/N) :')
        if z.lower() == 'y':
            z = input('Search with country name or country code ? (1/2) :')
            if z == '1':
                x = input('Enter name closest to original \n: eg("ndia" will display output "India") \n |> ')
                refresh_data()
                search('Country',x,data)
            elif z=='2':
                x = input('Enter code closest to original |> ')
                refresh_data()
                search('CountryCode',x,data)
            else:
                print('Enter Valid option')
                continue
        elif z.lower()=='n':
            break
        else:
            print('Enter Valid option')
            continue
def search(param,value,data):
    count=0
    L=[]
    for i in data['Countries']:
        if value.upper() in i[param].upper():
            count +=1
            L.append(i)
    while True:
        print(f'{count} Countries with {param} similar to {value} found')
        z=input('Do you want to print them ?(Y/N) :')
        if z.lower() == 'y':
            for i in L:
                decor(i)
            break
        elif z.lower() == 'n':
            break
        else:
            print('Enter valid option')
            continue
def decor(data):
    print('\n')
    for i in data.keys():
        print(f'{i} : {data[i]}')
    print('~'*40)
    if data['NewConfirmed'] !=0:
        print(f"Recovered percentage : {(int((data['TotalRecovered'] * 100 )/data['TotalConfirmed'])*100)/100} %")
        print(f"Recovery rate : {(int((data['NewRecovered'] * 100 )/data['NewConfirmed'])*100)/100} %")
    elif data['TotalConfirmed'] !=0:
        print(f"Recovered percentage : {(int((data['TotalRecovered'] * 100 )/data['TotalConfirmed'])*100)/100} %")
        print(f"Recovery rate : 100.0 %")
    else:
        print(f"Recovered percentage : 100.0 % ")
        print(f"Recovery rate : 100.0 %")
    print('\n')
    print('=='*20)

while True:
    try:
        refresh_data()
        display_data(data)
    except KeyboardInterrupt:
        print('\n\n')
        print('Keyboard Interrupt')
        print('Exiting....')
        break