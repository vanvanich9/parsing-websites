import sqlite3
import uuid as uuid_lib
from hashlib import sha256


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