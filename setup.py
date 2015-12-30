from setuptools import setup, find_packages


setup(
    name='sublime_plugin_tests_base',
    version='1.0.0',
    description='Base layer for testing and assertion frameworks against Sublime Text',
    long_description=open('README.rst').read(),
    keywords=[
        'sublime',
        'plugin',
        'test',
        'assert'
    ],
    author='Todd Wolfson',
    author_email='todd@twolfson.com',
    url='https://github.com/twolfson/sublime-plugin-tests-base',
    download_url='https://github.com/twolfson/sublime-plugin-tests-base/archive/master.zip',
    packages=find_packages(),
    license='UNLICENSE',
    install_requires=open('requirements.txt').readlines(),
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Topic :: Text Editors'
    ]
)
