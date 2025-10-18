from sqlalchemy import create_engine 
from sqlalchemy import text, inspect

class SubjectAPI:
    __scripts = {
        "delete_by_subject_title": text("DELETE FROM subject WHERE subject_title = :subject_to_delete"),
        "insert_new": text("INSERT INTO subject (\"subject_title\") values (:new_subject)"),
        "update_id":text("UPDATE subject SET subject_id = :new_id WHERE subject_title = :subject_to_update")
      }
    
    def __init__(self, connection_string):
                self.__db=create_engine(connection_string)

    def delete(self, subject_to_delete):
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete_by_subject_title"], {"subject_to_delete": subject_to_delete})
        conn.commit()
        conn.close()

    def create(self, new_subject):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert_new"], {"new_subject": new_subject})
        conn.commit()
        conn.close()

    def update(self, subject_to_update, new_id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["update_id"], {"subject_to_update": subject_to_update, "new_id":new_id})
        conn.commit()
        conn.close()  

