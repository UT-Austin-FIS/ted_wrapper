ted_wrapper
===========

This tool is a wrapper for the TED system to be used for directory lookups.


Installation
============

To bring this into a PyPE project you will need to add a new svn:externals property.

If you are using Tortoise:
* Right click on the main project folder.
* TortoiseSVN > Properties
* New... > Externals
* New...
* Local path: extra/ted
* URL: https://github.com/UT-Austin-FIS/ted_wrapper/tags/v1.1/ted
* OK

* Exit out of Tortoise, and you're done.


Backwards Compatibility
=======================

PyPE applications that currently use the ted lookups in versions of infrastructure 
prior to 1.8 will not need to change their code, but will need to add a new svn:externals 
property in order to continue making those calls once they upgrade to 1.8. See Installation.


Use
===

There are two methods in the ted_lookup module (by_eid and by_uin), and they both require 
these paramters:

eid or uin: The identifier of the person you are looking up
addl_attrs: There is a standard set of directory info that is brought back for all lookups
            as defined in ted.py. However, you can request that additional directory info 
            be brought back.  See http://www.utexas.edu/its/help/ted/1064 for the full set of 
            available attributes.
ted_eid: Your application's service EID which has been authorized to query TED.
ted_pass: The password associated with the ted_eid.
ted_host: The url of the TED service.

Example lookup by EID:

```python
from ted import ted_lookup

directory_info = ted_lookup.by_eid(
    eid='foobar',
    addl_attrs=[
        'telephoneNumber',
        'utexasEduPersonOfficeLocation',
        ],
    ted_eid=settings.TED_EID,
    ted_pass=settings.TED_PASSWORD,
    ted_host=settings.TED_HOSTNAME,
    )
```

Gotchas
=======
VirtualEnv on Windows
---------------------
This project depends on simpleldap, which itself depends on python-ldap. However, pip install simpleldap will likely fail in most Windows environments, even if it is set up with a compiler. 

The solution is to download an appropriate .exe installer and use easy_install to 
install it within the virtualenv, 
[as documented on stackoverflow](http://stackoverflow.com/questions/15918188/how-to-install-python-ldap-on-a-python-2-7-virtualenv-on-windows-without-compili). 
After installing python-ldap, you can pip install this project via
    pip install -e <path-to-ted-wrapper>
If you want to be able to run the tests, use
    pip install -e <path-to-ted-wrapper>[tests]

Release Notes
=============
v1.2 - Added django subpackage with ted_lookup module that uses Django settings.
v1.1 - added a new method to a returned person object - is_restricted().
