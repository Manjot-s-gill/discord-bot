import requests
import json

coc_clan_tags = ['QJ8YQG2','9Q9V8YLJ','Q8RPRYC9','8QYLVVRC','QGC0LVUU','22CPJQVCU','228VQ0PQC','YGG9GL8C','LQRPQ2Q2','PUJRCQGU','22RRPUQLQ','L8GR0JRU','JJRC08J0','LRYLQ09Y','QVL892PC', '29PUUJ8RU']

cr_clan_tags = ['PJPQLVYG','PPRJ8RPQ','PUQ99L0R','YJRGCUUL', 'Y289LP00']

#----------------------------------------------

def clan_info():

    headers = {
        'Accept' : 'application/json',
        'authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNjZTNmYTZmLTJmMDMtNDRjMi1hYTU3LTBmMjM1MWVlYjk5YSIsImlhdCI6MTU5MTc3MDk2NSwic3ViIjoiZGV2ZWxvcGVyLzUxNGYzNzhiLTM5MjEtODdjMS1jNjdiLTU5YzdkMDFkZjcxOCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy4yMTcuMTIzLjIxMiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.6Ez52GWrl7n2gASZdGwGMqG1n1h7-JIhvHV92BMc_XT8voJugqwSv58mfZB5huoA661fin9S6KyPhx3pOQNO9g'
    }
    #--------------Clash of Clans--------------#

    # Requesting for clan information through API.
    f = open('clanInfo.txt', 'w')
    f.write("Clash of Clans:\n\n")
    for coc in coc_clan_tags:
        response = requests.get('https://api.clashofclans.com/v1/clans?name=%23' + coc, headers=headers)
        claninfo = response.json()

    # Parsing JSON response and writing data into file.
        for item in claninfo['items']:
            json.dump(item["members"], f, indent= 2)
            f.write('/50 ClanName:')
            json.dump(item["name"], f, indent= 2)
            f.write(' Tag:')
            json.dump(item['tag'], f, indent= 2)
            f.write(' Focus: ')
            for labels in item['labels']:
                 json.dump(labels['name'], f, indent= 2)
                 f.write(' ')
        f.write('\n')
        f.write('\n')

    #--------------Clash Royale-----------------#
    headers = {
        'Accept' : 'application/json',
        'authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjE3NGRjZWQ1LWE0NWUtNDZjYi04YTdlLTMyYTJjNTNiZGNjNiIsImlhdCI6MTU5MTc3OTU2OSwic3ViIjoiZGV2ZWxvcGVyLzk4MDNiYmRhLWY2ZGYtZmRlNi05MjNlLTZkYjljYTFhMGFiNiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMDMuMjE3LjEyMy4yMTIiXSwidHlwZSI6ImNsaWVudCJ9XX0.nuYD9DH51h2mcT81uU-xaztHxoxYibUdAQywbBHGBNXlokD9VTKFYFrrrp8uaTcI5y1jORRAXMKiZ0Lye49GaA'
    }

    f.write('Clash Royale:\n\n')
    for cr in cr_clan_tags:
        ress = requests.get('https://api.clashroyale.com/v1/clans?name=%23' + cr, headers = headers)
        cr_clans = ress.json()

        for item in cr_clans['items']:
            json.dump(item["members"], f, indent= 2)
            f.write('/50 ClanName:')
            json.dump(item["name"], f, indent= 2)
            f.write(' Tag:')
            json.dump(item['tag'], f, indent= 2)
            f.write(' Donations: ')
            json.dump(item['donationsPerWeek'], f, indent= 2)
        f.write('\n')
        f.write('\n')

    #---------------Brwal Stars-------------------#
    f.write('Brawl Stars:\n\n')
    f.write('Name: "Reddit Yankee" Tag: "JRPUCV" Required Trophies: 1000')
#----------------------------------------------
clan_info()