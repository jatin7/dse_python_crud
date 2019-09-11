#!/usr/bin/env python3
from ip_address import Connection

# this is a delete statement in python
connection = Connection()
output = connection.session.execute(
    "DELETE FROM killrvideo.user_credentials WHERE email = %s",
    ['cv@datastax.com']
)
print(output)
connection.close()