import sqlite3
import uuid as uuid_lib
from hashlib import sha256
from ..schemas import ParsingElementData


ROUTE_TO_DATABASE = "app/database/database.db"


def use_database(coroutine):

    def wrapper(*args, **kwargs):
        connection = sqlite3.connect(ROUTE_TO_DATABASE)
        cursor = connection.cursor()
        result = coroutine(cursor, *args, **kwargs)
        connection.commit()
        cursor.close()
        connection.close()
        return result
    
    return wrapper


@use_database
def db_get_user_by_uuid(cursor, uuid):
    cursor.execute(
        '''
        SELECT uuid, username FROM users 
        WHERE uuid = ?
        ''', (uuid,)
    )
    result = cursor.fetchone()
    return result


@use_database
def db_get_user(cursor, username, password):
    hash = sha256()
    hash.update(password.encode())
    hash_password = hash.hexdigest()
    cursor.execute(
        '''
        SELECT uuid, username FROM users 
        WHERE username = ? AND hash_password = ?
        ''', (username, hash_password)
    )
    result = cursor.fetchone()
    return result


@use_database
def db_add_user(cursor, username, password):
    count_tries = 0
    hash = sha256()
    hash.update(password.encode())
    hash_password = hash.hexdigest()
    while count_tries < 5:
        try:
            uuid = str(uuid_lib.uuid4())
            cursor.execute(
                '''
                INSERT INTO users (uuid, username, hash_password)
                VALUES (?, ?, ?)
                ''', (uuid, username, hash_password)
            )
            break
        except:
            count_tries += 1
    if count_tries == 5:
        return False
    return True


@use_database
def db_delete_user_by_uuid(cursor, uuid):
    try:
        cursor.execute(
            '''
            DELETE FROM users 
            WHERE uuid = ?
            ''', (uuid,)
        )
        return True
    except:
        return False


@use_database
def db_delete_user(cursor, username, password):
    hash = sha256()
    hash.update(password.encode())
    hash_password = hash.hexdigest()
    try:
        cursor.execute(
            '''
            DELETE FROM users 
            WHERE username = ? AND hash_password = ?
            ''', (username, hash_password)
        )
        return True
    except:
        return False


@use_database
def db_get_parsing_ids(cursor, uuid):
    cursor.execute(
        '''
        SELECT id, url FROM history 
        WHERE uuid = ?
        ''', (uuid,)
    )
    result = cursor.fetchall()
    return result


@use_database
def db_get_parsing_result(cursor, uuid, id):
    cursor.execute(
        '''
        SELECT * FROM history 
        WHERE uuid = ? AND id = ?
        ''', (uuid, id)
    )
    result = cursor.fetchone()
    return result


@use_database
def db_add_parsing_result(cursor, uuid, data: ParsingElementData, url):
    count_tries = 0
    while count_tries < 5:
        try:
            cursor.execute(
                '''
                INSERT INTO history (
                id, uuid, url,
                first_p, first_v, 
                second_p, second_v, 
                third_p, third_v, 
                fourth_p, fourth_v,
                fifth_p, fifth_v,
                sixth_p, sixth_v, 
                seventh_p, seventh_v,
                eighth_p, eighth_v,
                ninth_p, ninth_v,
                tenth_p, tenth_v
                ) 
                VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                    ?, ?, ?
                )
                ''', (db_get_last_notice() + 1, uuid, url,
                    data.elements[0].word, data.elements[0].value,
                    data.elements[1].word, data.elements[1].value,
                    data.elements[2].word, data.elements[2].value,
                    data.elements[3].word, data.elements[3].value,
                    data.elements[4].word, data.elements[4].value,
                    data.elements[5].word, data.elements[5].value,
                    data.elements[6].word, data.elements[6].value,
                    data.elements[7].word, data.elements[7].value,
                    data.elements[8].word, data.elements[8].value,
                    data.elements[9].word, data.elements[9].value,
                    )
            )
            return True
        except:
            return False


@use_database
def db_delete_parsing_result(cursor, uuid, id):
    cursor.execute(
        '''
        DELETE FROM history 
        WHERE uuid = ? AND id = ?
        ''', (uuid, id)
    )
    result = cursor.fetchall()
    return result


@use_database
def db_get_last_notice(cursor):
    cursor.execute(
        '''
        SELECT * FROM history 
        '''
    )
    result = cursor.fetchall()
    max_id = 0
    for el in result:
        max_id = max(el[0], max_id)
    return max_id