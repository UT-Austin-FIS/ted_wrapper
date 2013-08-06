from unittest import TestCase
from mock import patch
from ted import ted_lookup, ted
from ldap import INVALID_CREDENTIALS
from ted_data import ted_data

HOSTNAME = "entdir.utexas.edu"


class LookupTests(TestCase):
    """
    These tests are primarily centered around the expected behavior of a call
    to the lookup methods, so in most of them we're mocking out the actual ted
    connection, and returning the fixture data.
    """

    def test_lookup_with_invalid_creds(self):
        # This test makes an actual ted call, as a minimal integration/API test.
        self.assertRaises(
            INVALID_CREDENTIALS,
            ted_lookup.by_eid,
            eid='foobar',
            ted_eid='foo',
            ted_pass='bar',
            ted_host=HOSTNAME,
            )

    @patch('ted.ted_lookup.TED_CONNECTION', spec=True)
    def test_lookup_by_eid(self, mock_connection):
        test_connection = mock_connection.return_value
        test_connection.get_by_eid.return_value = ted_data

        foo = ted_lookup.by_eid(
            'foobar',
            ted_eid='foo',
            ted_pass='bar',
            ted_host=HOSTNAME,
            )

        self.assertEqual(foo['eid'], ted_data['utexasEduPersonEid'][0])
        self.assertEqual(foo['uin'], ted_data['utexasEduPersonUin'][0])
        self.assertEqual(foo['name'], ted_data['cn'][0])
        self.assertEqual(foo['ted_data'], ted_data)

    @patch('ted.ted_lookup.TED_CONNECTION', spec=True)
    def test_lookup_by_uin(self, mock_connection):
        test_connection = mock_connection.return_value
        test_connection.get_by_uin.return_value = ted_data

        foo = ted_lookup.by_uin(
            '1234567891234567',
            ted_eid='foo',
            ted_pass='bar',
            ted_host=HOSTNAME,
            )

        self.assertEqual(foo['eid'], ted_data['utexasEduPersonEid'][0])
        self.assertEqual(foo['uin'], ted_data['utexasEduPersonUin'][0])
        self.assertEqual(foo['name'], ted_data['cn'][0])
        self.assertEqual(foo['ted_data'], ted_data)

    @patch('ted.ted_lookup.TED_CONNECTION', spec=True)
    def test_lookup_with_addl_attrs(self, mock_connection):
        test_connection = mock_connection.return_value
        test_connection.get_by_eid.return_value = ted_data

        foo = ted_lookup.by_eid(
            'foobar',
            addl_attrs='telephoneNumber',
            ted_eid='foo',
            ted_pass='bar',
            ted_host=HOSTNAME,
            )

        ted_data['telephoneNumber'] = '512-512-1512'

        self.assertEqual(foo['eid'], ted_data['utexasEduPersonEid'][0])
        self.assertEqual(foo['uin'], ted_data['utexasEduPersonUin'][0])
        self.assertEqual(foo['name'], ted_data['cn'][0])
        self.assertEqual(foo['ted_data'], ted_data)
        self.assertEqual(
            foo['ted_data']['telephoneNumber'],
            ted_data['telephoneNumber'],
            )

    def test_alias_data(self):
        foo = ted_lookup.alias_data(ted_data)

        self.assertEqual(foo['eid'], ted_data['utexasEduPersonEid'][0])
        self.assertEqual(foo['uin'], ted_data['utexasEduPersonUin'][0])
        self.assertEqual(foo['name'], ted_data['cn'][0])
        self.assertEqual(foo['ted_data'], ted_data)


class TedConnectionTests(TestCase):
    # TODO: expand these tests

    def test_anonymous_connection(self):
        # This test makes an actual ted call, as a minimal integration/API test.
        test_connection = ted.TEDConnection(
            service=False,
            hostname=HOSTNAME,
            )
        self.assertTrue(isinstance(test_connection, ted.TEDConnection))


class TedLDAPItemTests(TestCase):
    # TODO: expand these tests
    pass
