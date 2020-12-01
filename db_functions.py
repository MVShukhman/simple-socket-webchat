from hashlib import md5
import psycopg2


def get_conn():
    conn = psycopg2.connect(dbname="testdb", user="shukhman", password="password", host="localhost", port="5432")
    return conn


def login_exists(value):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(f"SELECT t.login FROM public.\"Users\" t WHERE login='{value}'")
    ans = len(cursor.fetchall())
    cursor.close()
    conn.close()
    return ans > 0


def user_check(user_login, user_password):
    hashed = md5(user_password.encode()).hexdigest()
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(f"SELECT t.login FROM public.\"Users\" t WHERE login='{user_login}' and hashed_password='{hashed}'")
    ans = len(cursor.fetchall())
    cursor.close()
    conn.close()


def create_user(login, password):
    hashed = md5(password.encode()).hexdigest()
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO public.\"Users\" (login, hashed_password) VALUES ('{login}', '{hashed}');")
    conn.commit()
    cursor.close
    conn.close()