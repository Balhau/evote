from distutils.core import setup
import os
import codecs
from setuptools import setup, find_packages


pname="evote"

#packages=[pname]+[pname+ "." + name
#	for name in os.listdir(os.path.join(pname)) if os.path.isdir(os.path.join(pname, name))]

current_dir=os.path.dirname(__file__)

with codecs.open(os.path.join(current_dir,'README.md'),'r','utf8') as readme_file:
		long_description=readme_file.read()

setup(	name='evote',
	version='1.0',
	url='https://git.balhau.net/',
	license='MIT License',
	description='A proof of concept of a idea to Electronic Vote',
	long_description=long_description,
	packages=find_packages(),
    test_suite="tests"

)
