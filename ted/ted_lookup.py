from ted_connection import get_ted_connection

TED_CONNECTION = get_ted_connection

def by_eid(eid, addl_attrs=None, ted_eid=None, ted_pass=None, ted_host=None):
    """
    addl_attrs: any directory information that you would like to return about
    a user that is not already a part of the attributes list defined in
    TEDConnection
    """
    connection = TED_CONNECTION(ted_eid, ted_pass, ted_host)
    ted_data = connection.get_by_eid(eid, attrs=addl_attrs)
    return alias_data(ted_data)

def by_uin(uin, addl_attrs=None, ted_eid=None, ted_pass=None, ted_host=None):
    """
    addl_attrs: any directory information that you would like to return about
    a user that is not already a part of the attributes list defined in
    TEDConnection
    """
    connection = TED_CONNECTION(ted_eid, ted_pass, ted_host)
    ted_data = connection.get_by_uin(uin, attrs=addl_attrs)
    return alias_data(ted_data)

def alias_data(ted_data):
    data = {}
    data['eid'] = ted_data['utexasEduPersonEid'][0]
    data['name'] = ted_data['cn'][0]
    data['uin'] = ted_data['utexasEduPersonUin'][0]
    data['ted_data'] = ted_data
    return data
