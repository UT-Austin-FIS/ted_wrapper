from __future__ import absolute_import
import os
try:
    from unittest import skipIf
except ImportError:
    import unittest2 as unittest
else:
    del skipIf
    import unittest


os.environ['DJANGO_SETTINGS_MODULE'] = 'ted.ted_tests.django.settings'
SKIP_TESTS = False
try:
    from django.conf import settings
except ImportError:
    print 'Skipping tests involving django'
    SKIP_TESTS = True


if not SKIP_TESTS:
    from mock import Mock, patch
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
                                            ted_host=settings.TED_HOSTNAME)

    @patch('ted.ted_lookup.by_uin')
    def test_by_uin_passes_ted_settings_correctly(self, mock_lookup):
        django_ted_lookup.by_uin(self.uin, self.addl_attrs)
        mock_lookup.assert_called_once_with(self.uin,
                                            self.addl_attrs,
                                            ted_eid=settings.TED_EID,
                                            ted_pass=settings.TED_PASSWORD,
                                            ted_host=settings.TED_HOSTNAME)
