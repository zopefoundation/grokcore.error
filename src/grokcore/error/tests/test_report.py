import logging
import sys
import zope.component
import zope.error.interfaces
import grokcore.error
import grokcore.error.testing

class FauxRequest(object):

    def __init__(self, url):
        self.URL = url

class TestErrorReporting(grokcore.error.testing.TestCase):

    def test_raising(self):
        eru = grokcore.error.LoggingErrorReporting()
        with grokcore.error.testing.Logger() as log:
            try:
                raise Exception('test raising an Exception')
            except Exception:
                eru.raising(sys.exc_info())
        self.assertEqual(1, len(log.records))
        self.assertEqual('grokcore.error', log.records[0].name)
        self.assertEqual('ERROR', log.records[0].levelname)
        self.assertEqual(
            """\
            Exception test raising an Exception
            Traceback (most recent call last):
             ...
            raise Exception('test raising an Exception')
            Exception: test raising an Exception
            """,
            log.format(log.records[0]))

    def test_raising_with_request(self):
        eru = grokcore.error.LoggingErrorReporting()
        with grokcore.error.testing.Logger() as log:
            try:
                raise Exception('test raising an Exception')
            except Exception:
                eru.raising(sys.exc_info(), request=FauxRequest('http://foo'))
        self.assertEqual(1, len(log.records))
        self.assertEqual('grokcore.error', log.records[0].name)
        self.assertEqual('ERROR', log.records[0].levelname)
        self.assertEqual(
            """\
            Exception test raising an Exception (URL: http://foo)
            Traceback (most recent call last):
             ...
            raise Exception('test raising an Exception')
            Exception: test raising an Exception
            """,
            log.format(log.records[0]))

    def test_raising_as_info(self):
        eru = grokcore.error.LoggingErrorReporting(
            info_level_errors=('__builtin__.Exception',))
        with grokcore.error.testing.Logger() as log:
            try:
                raise Exception('test raising an Exception')
            except Exception:
                eru.raising(sys.exc_info())
        self.assertEqual(1, len(log.records))
        self.assertEqual('grokcore.error', log.records[0].name)
        self.assertEqual('INFO', log.records[0].levelname)
        self.assertEqual(
            """Exception test raising an Exception""",
            log.format(log.records[0]))

class TestErrorReportingUtility(grokcore.error.testing.TestCase):
    layer = grokcore.error.testing.layer

    def test_utility_registered(self):
        eru = zope.component.getUtility(
            zope.error.interfaces.IErrorReportingUtility)
        self.assertTrue(isinstance(eru, grokcore.error.LoggingErrorReporting))
