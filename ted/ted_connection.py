from ted import TEDConnection
from ldap import SERVER_DOWN # @UnresolvedImport

ted_connection = None

def get_ted_connection(eid, password, hostname):
    global ted_connection

    if ted_connection is not None:
        try:
            ted_connection.connection.whoami_s()
            return ted_connection
        except SERVER_DOWN:
            pass

    ted_connection = TEDConnection(
        eid=eid,
        password=password,
        hostname=hostname,
        )
    return ted_connection
