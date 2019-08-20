#!/usr/bin/env python3
from ip_address import Connection

# this is a update statement in python
connection = Connection()
output = connection.session.execute(
    "UPDATE killrvideo.advocates SET super_power = %s WHERE region = %s AND city = %s AND last_name = %s AND first_name = %s",
    ('wormhole time travel', 'North Carolina', 'Charlotte', 'Veale', 'Cristina')
)
print(output)
connection.close()