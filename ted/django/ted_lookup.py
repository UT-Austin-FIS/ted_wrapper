from __future__ import absolute_import

from django.conf import settings

from ted import ted_lookup as main_lookup

def by_eid(eid, addl_attrs=None):
    return main_lookup.by_eid(
        eid,
        addl_attrs,
        ted_eid=settings.TED_EID,
        ted_pass=settings.TED_PASSWORD,
        ted_host=settings.TED_URL,
    )

def by_uin(uin, addl_attrs=None):
    return main_lookup.by_uin(
        uin,
        addl_attrs,
        ted_eid=settings.TED_EID,
        ted_pass=settings.TED_PASSWORD,
        ted_host=settings.TED_URL,
    )
