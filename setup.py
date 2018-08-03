from setuptools import setup


setup(
    name='nvdbapi',
    version='0.0.2',
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
        'git+https://github.com/jswhit/pyproj.git@429a4fe6fa404ba1bc1c0a88bee68c1a30a9b6f9#egg=pyproj',
    ]
)
