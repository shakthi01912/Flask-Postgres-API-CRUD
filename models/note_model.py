from utils.db_utils import db_connection

def create_table():
    dbConn = db_connection()
    if dbConn is None:
        return  
    dbCursor = dbConn.cursor()
    
    try:
        dbCursor.execute(
            '''CREATE TABLE IF NOT EXISTS notewithenv (
                id SERIAL PRIMARY KEY,
                note_name VARCHAR(255) NOT NULL,
                note_description VARCHAR(255)
            );
            ''')
        dbConn.commit()
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        dbCursor.close()
        dbConn.close()

def insert_note_db(name_input, description_input):
    dbConn = db_connection()
    if dbConn is None:
        return None

    cur = dbConn.cursor()
    try:
        cur.execute('INSERT INTO notewithenv (note_name, note_description) VALUES (%s, %s) RETURNING id;',
                    (name_input, description_input))
        note_id = cur.fetchone()[0]
        dbConn.commit()
        return note_id
    except Exception as e:
        dbConn.rollback()
        print(f"Error inserting note: {e}")
        return None
    finally:
        cur.close()
        dbConn.close()

def update_note_db(note_id, name_input, description_input):
    dbConn = db_connection()
    if dbConn is None:
        return False
    
    cur = dbConn.cursor()
    try:
        cur.execute('SELECT * FROM notewithenv WHERE id = %s;', (note_id,))
        existing_note_id = cur.fetchone()
        if existing_note_id:
            cur.execute('UPDATE notewithenv SET note_name = %s, note_description = %s WHERE id = %s;',
                        (name_input, description_input, note_id))
            dbConn.commit()
            return True
        return False
    except Exception as e:
        dbConn.rollback()
        print(f"Error updating note: {e}")
        return False
    finally:
        cur.close()
        dbConn.close()

def delete_note_db(note_id):
    dbConn = db_connection()
    if dbConn is None:
        return False

    cur = dbConn.cursor()
    try:
        cur.execute('DELETE FROM notewithenv WHERE id = %s;', (note_id,))
        dbConn.commit()
        return cur.rowcount > 0
    except Exception as e:
        dbConn.rollback()
        print(f"Error deleting note: {e}")
        return False
    finally:
        cur.close()
        dbConn.close()

def get_all_notes_db():
    dbConn = db_connection()
    if dbConn is None:
        return None

    cur = dbConn.cursor()
    try:
        cur.execute('SELECT * FROM notewithenv;')
        all_records = cur.fetchall()
        return [{'id': record[0], 'note_name': record[1], 'note_description': record[2]} for record in all_records]
    except Exception as e:
        print(f"Error fetching notes: {e}")
        return None
    finally:
        cur.close()
        dbConn.close()