# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import rest_web
import zipcodes




# Press the green button in the gutter to run the script.
##Main Fucntion########################
if __name__ == '__main__':
    conn = connect_to_sql()
    cursor = conn.cursor()
    zipcodes.run()
    rest_web.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
