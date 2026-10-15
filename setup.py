import os

from setuptools import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.rst')
    + '\n' +
    read('CHANGES.rst')
)

setup(
    name='grokcore.error',
    version='5.1.dev0',
    author='Grok Team',
    author_email='zope-dev@zope.dev',
    url='https://github.com/zopefoundation/grokcore.error',
    download_url='https://pypi.org/project/grokcore.startup',
    description='Error reporting utility for Grok projects.',
    long_description=long_description,
    license='ZPL',
    keywords='zope zope3 grok error reporting utility',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Zope :: 3',
    ],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.11',
    install_requires=[
        'grokcore.component',
        'setuptools',
        'zope.component',
        'zope.configuration',
        'zope.error',
        'zope.interface',
        'zope.publisher',
    ],
    extras_require={'test': [
        'zope.testing',
        'zope.testrunner >= 6.4',
    ]},
)
