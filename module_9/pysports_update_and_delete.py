'''
Jeremy Johnson
CYBR410
7/25/2022
Assignment 9.3
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

def show_players(cursor, title):
    cursor.execute('select player_id, first_name, last_name, team_name from player inner join team on player.team_id = team.team_id')
    players = cursor.fetchall()
    print("\n -- {} --".format(title))
    for player in players:
        print("Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))


try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    add_player = ("insert into player(first_name, last_name, team_id)values(%s, %s, %s)")
    player_data = ("Smeagol", "Shire Folk", 1)

    cursor.execute(add_player, player_data)
    db.commit()
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    update_player = ("update player set team_id =2, first_name = 'Gollum', last_name = 'Ringer Stealer' where first_name = 'Smeagol'")

    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    delete_player = ("delete from player where first_name = 'Gollum'")
    cursor.execute(delete_player)
    show_players(cursor,"DISPLAYING PLAYERS AFTER DELETE")


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
