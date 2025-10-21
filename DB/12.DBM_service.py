from DBManager import DBManager

dbm = DBManager()


def join(uName, uID, uPW, uEmail):

    if uName and uID and uPW and uEmail:

        pass
        sql = "INSERT INTO UserList (uName, uID, uPW, uEmail) VALUES (%s, %s, %s, %s)"
        dbm.DBOpen("localhost", "root", "ezen", "boardEX")
        dbm.DBClose()
        return dbm.RunSQL(sql, (uName, uID, uPW, uEmail))

    else:
        return False
    return null


name = "gang"
uID = "hea"
pw = "rin"
email = "email@email.com"

result = join(name, uID, pw, email)
if result:
    print("join success")
else:
    print("join fail")
