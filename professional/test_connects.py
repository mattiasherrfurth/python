#
# This function gets the login information out of a credentials file
#
def get_login_info(file):
    # Create an array of the lines of the file
    line = open(file, "r").readlines()
    # Create a new list to be used to append the cleaned / trimmed lines
    new_line = []
    # Loop through the file
    for a in line:
        # Get rid of any new lines ("enter")
        a = a.replace("\n", "")
        # Add the cleaned data to the new_line list
        new_line.append(a)
    # Set the username to be the first object
    username = new_line[0]
    # Set the password to be the second object
    password = new_line[1]

    # Return them
    return username, password

#
# This function gets databack from one of the database instances
# 
def get_data(database, username, password, sql_statement):
    # Import the Oracle package
    import cx_Oracle

    # If your database is Solumina, establish a connection
    if (database == 'Solumina'):
        # Create the dsn using Solumina's information
        dsn_tns = cx_Oracle.makedsn('SIREBRMES01.northgrum.com', '1521', 'ncdprod')
        # Establish a connection
        connection = cx_Oracle.connect(username, password, dsn_tns)

    # If your database is ORAD, establish a connection
    elif (database == 'ORAD'):
        # Create the dsn using ORAD's information
        dsn_tns = cx_Oracle.makedsn('uworad00.md.essd.northgrum.com', '1560', 'orad')
        # Establish a connection
        connection = cx_Oracle.connect(username, password, dsn_tns)
    
    # If neither, then that means you entered something bogus
    else:
        # Alert the user
        print("You did not enter a recognized database. Please use Solumina or ORAD")
    
    # Create a cursor object to navigate those data sources
    c = connection.cursor()
    # Execute the passed sql statement
    c.execute(sql_statement)

    # Print the returning dataset
    for row in c:
        print(row)
    
    # Close the connection
    connection.close()

#
# This function parses a .sql file and returns it as a string
#
def parseSQL(file):
    # Open the file
    fd = open(file, 'r')
    # Read the file
    sql = fd.read()
    # Close the file
    fd.close()

    # Return the string version of the file
    return sql

#
# Main function
#
def main():
    # Grab your username and password for solumina  
    solumina_username, solumina_pw = get_login_info('solumina_credentials.txt')
    # Create a sql statement
    solumina_sql = "SELECT SFMFG.RC_MIM_SPC_V.* FROM SFMFG.RC_MIM_SPC_V WHERE ((SFMFG.RC_MIM_SPC_V.PROGRAM LIKE 'JSF%') AND ROWNUM >= 1000)"
    # Get your data
    get_data('Solumina', solumina_username, solumina_pw, solumina_sql)

    # Grab your username and password for ORAD
    orad_username, orad_pw = get_login_info('orad_credentials.txt')
    # Create a sql statement
    # orad_sql = "SELECT DISTINCT * FROM TDWHPLNT"
    orad_sql = parseSQL('TDWHPLNT.sql')
    print(orad_sql)
    # Get your data
    get_data('ORAD', orad_username, orad_pw, orad_sql)

main()