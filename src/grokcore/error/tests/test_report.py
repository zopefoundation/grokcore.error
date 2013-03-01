import unittest
import sys
import zope.component
import zope.error.interfaces
import grokcore.error
import grokcore.error.testing

class TestErrorReportingUtility(grokcore.error.testing.TestCase):
    layer = grokcore.error.testing.layer

    def test_utility_registered(self):
        eru = zope.component.getUtility(
            zope.error.interfaces.IErrorReportingUtility)
        self.assertTrue(isinstance(eru, grokcore.error.LoggingErrorReporting))

    def test_raising(self):
        eru = zope.component.getUtility(
            zope.error.interfaces.IErrorReportingUtility)
        with grokcore.error.testing.Logger() as log:
            try:
                raise Exception('test raising an Exception')
            except Exception:
                eru.raising(sys.exc_info())
        self.assertEqual(1, len(log.records))
        self.assertEqual(
            """\
            Exception test raising an Exception
            Traceback (most recent call last):
            ...
            raise Exception('test raising an Exception')
            Exception: test raising an Exception
            """,
            log.records[0])
