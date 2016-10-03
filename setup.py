from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

try:
    import pypandoc
    long_description = pypandoc.convert_file(path.join(here, 'README.md'),
                                             format='markdown_github',
                                             to='rst',
                                             outputfile="README.rst")
except (ImportError, OSError) as error:
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='dollarpy',
    version='0.1.1',
    description='A python imlementation of the $P Point-Cloud Recognizer',
    long_description=long_description,
    url='https://github.com/sonovice/dollarpy',
    author='Simon Waloschek',
    author_email='simon.waloschek@posteo.de',
    license='LGPLv3+',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='gesture',
    py_modules=["dollarpy"],
)
