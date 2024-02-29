from setuptools import setup

setup(
    name='tle_calculations',
    packages=['tle_calculations'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sgp4',
        'scipy',
        'requests',
        'psycopg2',
        'skyfield',
        'psycopg2-binary',
    ],
)