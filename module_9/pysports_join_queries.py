'''
Jeremy Johnson
CYBR410
7/25/2022
Assignment 9.2
'''


from select import select
import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'pysports_user',
    'password':'MySQL8IsGreat!',
    'host' : 'localhost',
    'database' : 'pysports',
    'raise_on_warnings' : True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    cursor.execute('select player_id, first_name, last_name, team_name from player inner join team on player.team_id = team.team_id')

    players = cursor.fetchall()

    print("\n -- DISPLAYING PLAYER RECORDS --")

    for player in players:
        print("Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password is invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    db.close()
