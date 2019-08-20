#!/usr/bin/env python3
from ip_address import Connection

# this is a insert statement in python
connection = Connection()
output = connection.session.execute(
    "INSERT INTO killrvideo.advocates (first_name, last_name, region, city, super_power) VALUES (%s, %s, %s, %s, %s)",
    ('Cristina', 'Veale', 'North Carolina', 'Charlotte', 'time travel')
)
print(output)
connection.close()