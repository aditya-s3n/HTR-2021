import sqlite3
from typing import final
import uuid
from sqlite3.dbapi2 import connect

DATABASE_PATH = './applicants.db'

def init_applicant_table() -> None:
    '''Initializes the applicant table if not exist.
    '''

    statement = '''CREATE TABLE IF NOT EXISTS applicants (
                        uuid text,
                        name text,
                        email text,
                        education text,
                        employment text,
                        resume_path text
                    )'''

    connection = make_connection()
    cursor = connection.cursor()
    cursor.execute(statement)
    finalize_connection(connection)


def add_entry(uuid: str, name: str, email: str, education: str, employment: str, resume_path: str):
    statement = '''INSERT INTO applicants VALUES (?, ?, ?, ?, ?, ?)'''
    connection = make_connection()
    cursor = connection.cursor()
    cursor.execute(statement, (uuid, name, email, education, employment, resume_path))
    finalize_connection(connection)


def get_entry_by_uuid(uuid: str):
    statement = '''SELECT * FROM applicants WHERE uuid = ?'''
    connection = make_connection()
    cursor = connection.cursor()
    data = cursor.execute(statement, (uuid,)).fetchone()
    finalize_connection(connection)
    return data


def get_entry_by_name(name: str):
    statement = '''SELECT * FROM applicants WHERE name = ?'''
    connection = make_connection()
    cursor = connection.cursor()
    data = cursor.execute(statement, (name,)).fetchone()
    finalize_connection(connection)
    return data


def get_entry_by_email(email: str):
    statement = '''SELECT * FROM applicants WHERE email = ?'''
    connection = make_connection()
    cursor = connection.cursor()
    data = cursor.execute(statement, (email,)).fetchone()
    finalize_connection(connection)
    return data


def get_entries_by_education(education: str):
    statement = '''SELECT * FROM applicants WHERE education = ?'''
    connection = make_connection()
    cursor = connection.cursor()
    data = cursor.execute(statement, (education,)).fetchall()
    finalize_connection(connection)
    return data


def get_entries_by_employment(employment: str):
    statement = '''SELECT * FROM applicants WHERE employment = ?'''
    connection = make_connection()
    cursor = connection.cursor()
    data = cursor.execute(statement, (employment,)).fetchall()
    finalize_connection(connection)
    return data


def make_connection():
    return sqlite3.connect(DATABASE_PATH)


def finalize_connection(connection) -> None:
    connection.commit()
    connection.close()


def create_uuid() -> str:
    return str(uuid.uuid4())


if __name__ == '__main__':
    init_applicant_table()