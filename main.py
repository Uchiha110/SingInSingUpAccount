import eel
import time, sys, random
import mysql.connector
from mysql.connector import Error
import smtplib
from mainSettingsSingUpSingIn import *

eel.init('web/SingInSingUp')

pn_user = random.randint(100000000000, 999999999999)
pn_user = str(pn_user)

timeCallMessage = time.strftime('%dd.%mm.%yy')
tCM = timeCallMessage

# maun_Su.py

_uN = ''
@eel.expose
def userName(x):
    global _uN
    _uN = x

    if len(_uN) != 0:
        pass
    elif len(_uN) == 0:
        print('Please try again!')
        time.sleep(3)
        sys.exit() 

_uE = ''
@eel.expose
def userEmail(x):
    global _uE
    _uE = x

    if len(_uE) != 0:
        pass
    elif len(_uE) == 0:
        print('Please try again!')
        time.sleep(3)
        sys.exit()   

_uP = ''
@eel.expose
def userPassword(x):
    global _uP
    _uP = x

    if len(_uP) != 0:
        pass
    elif len(_uP) == 0:
        print('Please try again!')
        time.sleep(3)
        sys.exit()

_pN = ''
@eel.expose
def userPersonalNumber(x):
    global _pN
    _pN = x

    if len(_pN) != 0:
        pass
    elif len(_pN) == 0:
        print('Please try again!')
        time.sleep(3)
        sys.exit()

_uD = ''
@eel.expose
def userDay(x):
    global _uD
    _uD = x

    if len(_uD) != 0:
        pass
    elif len(_uD) == 0:
        print('Please try again!')
        time.sleep(3)
        sys.exit() 

_uM = ''
@eel.expose
def userMonth(x):
    global _uM
    _uM = x

    if len(_uM) != 0:
        pass
    elif len(_uM) == 0:
        print('Please try again!')
        time.sleep(3)
        sys.exit() 

_uY = ''
@eel.expose
def userYear(x):
    global _uY
    _uY = x

    if len(_uY) != 0:
        pass
    elif len(_uY) == 0:
        print('Please try again!')
        time.sleep(3)
        sys.exit()

@eel.expose
def call_message_email_SingUp():
    sender = myEmail
    password = myEmailPassword
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, _uE, f'Subject: Your personal number\nHello {_uN}! Please remember this code, with it you will be able to log into your account. It cannot be shown to other users.\n{pn_user}')

        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

@eel.expose
def verificationNumberAndEmail(x):
    email_PN = x
    if pn_user == email_PN:
        time.sleep(2)
    elif pn_user != email_PN:
        time.sleep(2)
        sys.exit()

@eel.expose
def callUserDataMySql_SingUp():
    try:
        connectdb = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
        )

        cursor = connectdb.cursor()

        createTableOrNot = """CREATE TABLE IF NOT EXISTS infoaccountuser ( 
                            id TINYINT AUTO_INCREMENT PRIMARY KEY, 
                            pn_user VARCHAR(225),
                            u_name VARCHAR(255),
                            u_email VARCHAR(255),
                            u_password VARCHAR(255),
                            dirth_d VARCHAR(20),
                            dirth_m VARCHAR(20),
                            dirth_y VARCHAR(20)
                            );"""
        cursor.execute(createTableOrNot)
        connectdb.commit()
        inset_info = f"""INSERT INTO infoaccountuser VALUES ( 
                NULL, 
                '{pn_user}',
                '{_uN}',
                '{_uE}',
                '{_uP}',
                '{_uD}',
                '{_uM}',
                '{_uY}'
                );"""
        cursor.execute(inset_info)
        connectdb.commit()

    except Error as _e:
        print(_e)

@eel.expose
def examUserDataMySql_SingInPN():
    try:
        connectdb = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
        )

        cursor = connectdb.cursor(buffered=True)

        examEmaildb = f'''SELECT `u_email` FROM `infoaccountuser` WHERE `u_email` = '{_uE}';'''
        cursor.execute(examEmaildb)
        connectdb.commit()
    
        examPersonalNumberdb = f'''SELECT `pn_user` FROM `infoaccountuser` WHERE `pn_user` = '{_pN}';'''
        cursor.execute(examPersonalNumberdb)
        connectdb.commit()

    except Error as _e:
        print(_e)

@eel.expose
def call_message_email_SingInPN():
    sender = myEmail
    password = myEmailPassword
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, _uE, f'Subject: Your account is logged in!\nYour account is signed in, you are logged in {tCM}')

        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

@eel.expose
def examUserDataMySql_SingInCM():
    try:
        connectdb = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
        )

        cursor = connectdb.cursor(buffered=True)

        examNamedb = f'''SELECT `u_name` FROM `info_account_user` WHERE `u_name` = '{_uN}';'''
        cursor.execute(examNamedb)
        connectdb.commit()
    
        examEmaildb = f'''SELECT `u_email` FROM `info_account_user` WHERE `u_email` = '{_uE}';'''
        cursor.execute(examEmaildb)
        connectdb.commit()

        examPassworddb = f'''SELECT `u_password` FROM `info_account_user` WHERE `u_password` = '{_uE}';'''
        cursor.execute(examPassworddb)
        connectdb.commit()

    except Error as _e:
        print(_e)

eel.start('SiOrSu.html', size=(1000, 400))
