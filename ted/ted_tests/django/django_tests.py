from __future__ import absolute_import
import os

SKIP_TESTS = False

def skip(msg):
    global SKIP_TESTS
    # print to stdout so that nosetests can capture if desired
    general_message = (
"""
    {msg}
    Unable to run Django-related tests:
        pip install <ted_wrapper_path>[tests]
    to install testing dependencies.
""")
    print general_message.format(msg=msg)
    SKIP_TESTS = True

try:
    from unittest import skipIf
except ImportError:
    try:
        import unittest2 as unittest
    except ImportError:
        skip("Unable to import unittest with skipIf.")
else:
    del skipIf
    import unittest

if not SKIP_TESTS:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'ted.ted_tests.django.settings'
    try:
        from django.conf import settings
    except ImportError:
        skip("Unable to import django settings.")


if not SKIP_TESTS:
    try:
        from mock import Mock, patch
    except ImportError:
        skip("Unable to import mock.")

if not SKIP_TESTS:
    from ted.django import ted_lookup as django_ted_lookup
    
    @unittest.skipIf(SKIP_TESTS, "Django not found; skipping Django tests.")
    class TedDjangoTestCase(unittest.TestCase):
        def setUp(self):
            self.eid = Mock()
            self.uin = Mock()
            self.addl_attrs = Mock()

        @patch('ted.ted_lookup.by_eid')
        def test_by_eid_passes_ted_settings_correctly(self, mock_lookup):
            django_ted_lookup.by_eid(self.eid, self.addl_attrs)
            mock_lookup.assert_called_once_with(self.eid,
                                                self.addl_attrs,
                                                ted_eid=settings.TED_EID,
                                                ted_pass=settings.TED_PASSWORD,
                                                ted_host=settings.TED_URL)

        @patch('ted.ted_lookup.by_uin')
        def test_by_uin_passes_ted_settings_correctly(self, mock_lookup):
            django_ted_lookup.by_uin(self.uin, self.addl_attrs)
            mock_lookup.assert_called_once_with(self.uin,
                                                self.addl_attrs,
                                                ted_eid=settings.TED_EID,
                                                ted_pass=settings.TED_PASSWORD,
                                                ted_host=settings.TED_URL)
