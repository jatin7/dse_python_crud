#!/usr/bin/env python3
from ip_address import Connection

# this is a delete statement in python
connection = Connection()
output = connection.session.execute(
    "DELETE FROM killrvideo.advocates WHERE region = %s AND city = %s AND last_name = %s AND first_name = %s",
    ('North Carolina', 'Charlotte', 'Veale', 'Cristina')
)
print(output)
connection.close()