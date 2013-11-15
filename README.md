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
* URL: https://github.com/UT-Austin-FIS/ted_wrapper/tags/v1.2/ted
* OK

* Exit out of Tortoise, and you're done.


Backwards Compatibility
=======================

PyPE applications that currently use the ted lookups in versions of infrastructure 
prior to 1.8 will not need to change their code, but will need to add a new svn:externals 
property in order to continue making those calls once they upgrade to 1.8. See Installation.

FIS Infrastructure will remove ted support in the 1.9 branch. You can achieve a 
similar effect by using ted.django support as described below.


Use
===

There are two methods in the ted_lookup module (by_eid and by_uin), and they both require 
these paramters:

eid or uin: The identifier of the person you are looking up
addl_attrs: There is a standard set of directory info that is brought back for all lookups
            as defined in ted.py. However, you can request that additional directory info 
            be brought back.  See http://www.utexas.edu/its/help/ted/1064 for the full set of 
            available attributes.

    ted_eid: [Your application's service EID which has been authorized to query TED.]
    ted_pass: [The password associated with the ted_eid.]
    ted_host: [The name of the TED server, e.g., 'myserver.bigu.edu'.]

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

Django
------
In Django projects, it may be more convenient to add the following fields to Django
settings:

```python
TED_EID: [the eid used to connect to the TED account]
TED_PASSWORD: [the password used to connect]
TED_HOSTNAME: [The name of the TED server, e.g., 'myserver.bigu.edu'.]
```

and then import ted_lookup as follows:

```python
from ted.django import ted_lookup

directory_info = ted_lookup.by_eid(
    eid='foobar',
    addl_attrs=[
        'telephoneNumber',
        'utexasEduPersonOfficeLocation',
        ],
    )

directory_info = ted_lookup.by_uin(
    eid='uin-value',
    addl_attrs=[
        'telephoneNumber',
        'utexasEduPersonOfficeLocation',
        ],
    )
```

The Django TED_ settings will implicitly be used.

Testing
=======
You can run the tests with 

    nosetests ted

If you pip install with the extra "test_support", the packages needed for running the 
tests will also be installed (including nose), e.g.,

    pip install -e <path-to-ted-wrapper>[test_support]

Gotchas
=======
VirtualEnv on Windows
---------------------
This project depends on simpleldap, which itself depends on python-ldap. However, pip install simpleldap will likely fail in most Windows environments, even if the Windows environment is set up to support compilation.

The easiest solution is to download an appropriate .exe installer and use easy_install 
to install it within the virtualenv, 
[as documented on stackoverflow](http://stackoverflow.com/questions/15918188/how-to-install-python-ldap-on-a-python-2-7-virtualenv-on-windows-without-compili). 
After installing python-ldap, you can pip install this project via

    pip install -e <path-to-ted-wrapper>

Release Notes
=============
v1.2
----
- Added django subpackage with ted_lookup module that uses Django settings. 
- Added setup.py support.

v1.1
----
- Added a new method to a returned person object - is_restricted().
