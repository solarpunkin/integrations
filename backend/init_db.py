import sqlite3

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"successful connection with sqlite version {sqlite3.sqlite_version}")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_stops(conn):
    stops = [
        (1, 'Koramangala', 12.935, 77.625),
        (2, 'Indiranagar', 12.978, 77.641),
        (3, 'HSR Layout', 12.912, 77.644),
        (4, 'Marathahalli', 12.959, 77.701),
        (5, 'Whitefield', 12.969, 77.75),
        (6, 'Electronic City', 12.845, 77.660),
        (7, 'Jayanagar', 12.929, 77.582),
        (8, 'JP Nagar', 12.906, 77.593),
        (9, 'Banashankari', 12.925, 77.546),
        (10, 'Malleshwaram', 12.998, 77.570),
        (11, 'BTM Layout', 12.915, 77.610),
        (12, 'Bellandur', 12.930, 77.678),
        (13, 'Sarjapur Road', 12.912, 77.684),
        (14, 'Hebbal', 13.035, 77.596),
        (15, 'Yelahanka', 13.100, 77.596),
    ]
    sql = ''' INSERT OR REPLACE INTO stops(stop_id,name,latitude,longitude)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, stops)
    conn.commit()

def insert_paths(conn):
    paths = [
        (1, 'Koramangala-Indiranagar', '1,2'),
        (2, 'HSR-Marathahalli', '3,4'),
        (3, 'Whitefield-Marathahalli', '5,4'),
        (4, 'ElectronicCity-HSR', '6,3'),
        (5, 'Jayanagar-JP Nagar', '7,8'),
        (6, 'Banashankari-Jayanagar', '9,7'),
        (7, 'Malleshwaram-Indiranagar', '10,2'),
        (8, 'Koramangala-HSR', '1,3'),
        (9, 'BTM-Koramangala', '11,1'),
        (10, 'Bellandur-Marathahalli', '12,4'),
        (11, 'Sarjapur-Bellandur', '13,12'),
        (12, 'Hebbal-Yelahanka', '14,15'),
    ]
    sql = ''' INSERT OR REPLACE INTO paths(path_id,path_name,stop_ids)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, paths)
    conn.commit()

def insert_routes(conn):
    routes = [
        (1, 1, 'KI-Morning-08:00', '08:00', 'LOGIN', 'Koramangala', 'Indiranagar', 'active'),
        (2, 1, 'KI-Evening-18:00', '18:00', 'LOGOUT', 'Indiranagar', 'Koramangala', 'active'),
        (3, 2, 'HM-Morning-09:00', '09:00', 'LOGIN', 'HSR Layout', 'Marathahalli', 'active'),
        (4, 2, 'HM-Evening-19:00', '19:00', 'LOGOUT', 'Marathahalli', 'HSR Layout', 'active'),
        (5, 3, 'WM-Morning-08:30', '08:30', 'LOGIN', 'Whitefield', 'Marathahalli', 'active'),
        (6, 3, 'WM-Evening-18:30', '18:30', 'LOGOUT', 'Marathahalli', 'Whitefield', 'active'),
        (7, 4, 'EH-Morning-09:30', '09:30', 'LOGIN', 'Electronic City', 'HSR Layout', 'active'),
        (8, 4, 'EH-Evening-19:30', '19:30', 'LOGOUT', 'HSR Layout', 'Electronic City', 'active'),
        (9, 5, 'JJ-Morning-08:45', '08:45', 'LOGIN', 'Jayanagar', 'JP Nagar', 'active'),
        (10, 5, 'JJ-Evening-18:45', '18:45', 'LOGOUT', 'JP Nagar', 'Jayanagar', 'active'),
        (11, 6, 'BJ-Morning-09:15', '09:15', 'LOGIN', 'Banashankari', 'Jayanagar', 'active'),
        (12, 6, 'BJ-Evening-19:15', '19:15', 'LOGOUT', 'Jayanagar', 'Banashankari', 'active'),
        (13, 7, 'MI-Morning-08:15', '08:15', 'LOGIN', 'Malleshwaram', 'Indiranagar', 'active'),
        (14, 7, 'MI-Evening-18:15', '18:15', 'LOGOUT', 'Indiranagar', 'Malleshwaram', 'active'),
        (15, 8, 'KH-Morning-09:45', '09:45', 'LOGIN', 'Koramangala', 'HSR Layout', 'active'),
        (16, 8, 'KH-Evening-19:45', '19:45', 'LOGOUT', 'HSR Layout', 'Koramangala', 'active'),
        (17, 9, 'BK-Morning-08:00', '08:00', 'LOGIN', 'BTM Layout', 'Koramangala', 'active'),
        (18, 9, 'BK-Evening-18:00', '18:00', 'LOGOUT', 'Koramangala', 'BTM Layout', 'deactivated'),
        (19, 10, 'BM-Morning-09:00', '09:00', 'LOGIN', 'Bellandur', 'Marathahalli', 'active'),
        (20, 10, 'BM-Evening-19:00', '19:00', 'LOGOUT', 'Marathahalli', 'Bellandur', 'active'),
        (21, 11, 'SB-Morning-08:30', '08:30', 'LOGIN', 'Sarjapur Road', 'Bellandur', 'active'),
        (22, 11, 'SB-Evening-18:30', '18:30', 'LOGOUT', 'Bellandur', 'Sarjapur Road', 'active'),
        (23, 12, 'HY-Morning-09:30', '09:30', 'LOGIN', 'Hebbal', 'Yelahanka', 'deactivated'),
        (24, 12, 'HY-Evening-19:30', '19:30', 'LOGOUT', 'Yelahanka', 'Hebbal', 'active'),
    ]
    sql = ''' INSERT OR REPLACE INTO routes(route_id,path_id,route_display_name,shift_time,direction,start_point,end_point,status)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, routes)
    conn.commit()

def insert_vehicles(conn):
    vehicles = [
        (1, 'KA-01-AB-1234', 'Bus', 50),
        (2, 'KA-02-BC-2345', 'Cab', 4),
        (3, 'KA-03-CD-3456', 'Bus', 40),
        (4, 'KA-04-DE-4567', 'Cab', 4),
        (5, 'KA-05-EF-5678', 'Bus', 30),
        (6, 'KA-01-FG-6789', 'Cab', 4),
        (7, 'KA-02-GH-7890', 'Bus', 50),
        (8, 'KA-03-HI-8901', 'Cab', 4),
        (9, 'KA-04-IJ-9012', 'Bus', 40),
        (10, 'KA-05-JK-0123', 'Cab', 4),
        (11, 'KA-01-KL-1111', 'Bus', 50),
        (12, 'KA-02-LM-2222', 'Cab', 4),
        (13, 'KA-03-MN-3333', 'Bus', 40),
        (14, 'KA-04-NO-4444', 'Cab', 4),
        (15, 'KA-05-OP-5555', 'Bus', 30),
    ]
    sql = ''' INSERT OR REPLACE INTO vehicles(vehicle_id,license_plate,type,capacity)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, vehicles)
    conn.commit()

def insert_drivers(conn):
    drivers = [
        (1, 'Ramesh', '1234567890'),
        (2, 'Suresh', '0987654321'),
        (3, 'Mahesh', '1122334455'),
        (4, 'Rajesh', '5566778899'),
        (5, 'Sathish', '9988776655'),
        (6, 'Girish', '6655443322'),
        (7, 'Karthik', '2233445566'),
        (8, 'Prakash', '8877665544'),
        (9, 'Manoj', '4455667788'),
        (10, 'Anil', '7788990011'),
        (11, 'Sunil', '1231231234'),
        (12, 'Vinod', '4321432156'),
        (13, 'Sandeep', '5432543210'),
        (14, 'Naveen', '6543654321'),
        (15, 'Pramod', '7654765432'),
    ]
    sql = ''' INSERT OR REPLACE INTO drivers(driver_id,name,phone_number)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, drivers)
    conn.commit()

def insert_daily_trips(conn):
    trips = [
        (1, 1, 'KI-Morning-08:00', 0.8, 'On Time'),
        (2, 2, 'KI-Evening-18:00', 0.6, 'Delayed'),
        (3, 3, 'HM-Morning-09:00', 0.9, 'On Time'),
        (4, 4, 'HM-Evening-19:00', 0.5, 'On Time'),
        (5, 5, 'WM-Morning-08:30', 0.7, 'Delayed'),
        (6, 6, 'WM-Evening-18:30', 0.8, 'On Time'),
        (7, 7, 'EH-Morning-09:30', 0.6, 'On Time'),
        (8, 8, 'EH-Evening-19:30', 0.9, 'Delayed'),
        (9, 9, 'JJ-Morning-08:45', 0.5, 'On Time'),
        (10, 10, 'JJ-Evening-18:45', 0.7, 'On Time'),
        (11, 1, 'KI-Morning-08:15', 0.2, 'On Time'),
        (12, 17, 'BK-Morning-08:00', 0.4, 'On Time'),
        (13, 19, 'BM-Morning-09:00', 0.1, 'Delayed'),
        (14, 21, 'SB-Morning-08:30', 0.0, 'On Time'),
        (15, 24, 'HY-Evening-19:30', 0.3, 'On Time'),
    ]
    sql = ''' INSERT OR REPLACE INTO daily_trips(trip_id,route_id,display_name,booking_status_percentage,live_status)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, trips)
    conn.commit()

def insert_deployments(conn):
    deployments = [
        (1, 1, 1, 1),
        (2, 2, 2, 2),
        (3, 3, 3, 3),
        (4, 4, 4, 4),
        (5, 5, 5, 5),
        (6, 6, 6, 6),
        (7, 7, 7, 7),
        (8, 8, 8, 8),
        (9, 9, 9, 9),
        (10, 10, 10, 10),
        (11, 11, 1, 2),
        (12, 12, 11, 11),
        (13, 13, 12, 12),
        (14, 15, 13, 13),
    ]
    sql = ''' INSERT OR REPLACE INTO deployments(deployment_id,trip_id,vehicle_id,driver_id)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, deployments)
    conn.commit()


def main():
    database = "backend/movi.db"

    sql_create_stops_table = """ CREATE TABLE IF NOT EXISTS stops (
                                        stop_id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        latitude real NOT NULL,
                                        longitude real NOT NULL
                                    ); """

    sql_create_paths_table = """CREATE TABLE IF NOT EXISTS paths (
                                    path_id integer PRIMARY KEY,
                                    path_name text NOT NULL,
                                    stop_ids text NOT NULL
                                );"""

    sql_create_routes_table = """CREATE TABLE IF NOT EXISTS routes (
                                    route_id integer PRIMARY KEY,
                                    path_id integer NOT NULL,
                                    route_display_name text NOT NULL,
                                    shift_time text NOT NULL,
                                    direction text NOT NULL,
                                    start_point text NOT NULL,
                                    end_point text NOT NULL,
                                    status text NOT NULL,
                                    FOREIGN KEY (path_id) REFERENCES paths (path_id)
                                );"""

    sql_create_vehicles_table = """CREATE TABLE IF NOT EXISTS vehicles (
                                    vehicle_id integer PRIMARY KEY,
                                    license_plate text NOT NULL,
                                    type text NOT NULL,
                                    capacity integer NOT NULL
                                );"""
    
    sql_create_drivers_table = """CREATE TABLE IF NOT EXISTS drivers (
                                    driver_id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    phone_number text NOT NULL
                                );"""

    sql_create_daily_trips_table = """CREATE TABLE IF NOT EXISTS daily_trips (
                                        trip_id integer PRIMARY KEY,
                                        route_id integer NOT NULL,
                                        display_name text NOT NULL,
                                        booking_status_percentage real NOT NULL,
                                        live_status text NOT NULL,
                                        FOREIGN KEY (route_id) REFERENCES routes (route_id)
                                    );"""
    
    sql_create_deployments_table = """CREATE TABLE IF NOT EXISTS deployments (
                                        deployment_id integer PRIMARY KEY,
                                        trip_id integer NOT NULL,
                                        vehicle_id integer NOT NULL,
                                        driver_id integer NOT NULL,
                                        FOREIGN KEY (trip_id) REFERENCES daily_trips (trip_id),
                                        FOREIGN KEY (vehicle_id) REFERENCES vehicles (vehicle_id),
                                        FOREIGN KEY (driver_id) REFERENCES drivers (driver_id)
                                    );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_stops_table)
        create_table(conn, sql_create_paths_table)
        create_table(conn, sql_create_routes_table)
        create_table(conn, sql_create_vehicles_table)
        create_table(conn, sql_create_drivers_table)
        create_table(conn, sql_create_daily_trips_table)
        create_table(conn, sql_create_deployments_table)
        
        # insert data
        insert_stops(conn)
        insert_paths(conn)
        insert_routes(conn)
        insert_vehicles(conn)
        insert_drivers(conn)
        insert_daily_trips(conn)
        insert_deployments(conn)

        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
