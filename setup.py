from setuptools import setup


setup(
    name='nvdbapi',
    version='0.0.1',
    url='http://github.com/HyreAS/nvdbapi/',
    license='MIT',
    maintainer='',
    maintainer_email='',
    description='',
    packages=['nvdbapi'],
    install_requires=[
        'six==1.11.0',
        'requests==2.18.4',
        'shapely==1.6.1',
        'xmltodict==0.11.0',
        'psycopg2==2.7.3.1',
        'pyproj==1.9.5.1',
    ],
)
