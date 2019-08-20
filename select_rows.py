#!/usr/bin/env python3
from ip_address import Connection

# this is a select statement in python
connection = Connection()
output = connection.session.execute("SELECT * FROM killrvideo.advocates WHERE region = %s AND city = %s AND last_name = %s AND first_name = %s",
('North Carolina', 'Charlotte', 'Veale', 'Cristina'))
for row in output:
    print(row)
connection.close()