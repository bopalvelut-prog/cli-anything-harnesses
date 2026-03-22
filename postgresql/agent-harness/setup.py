from setuptools import setup
setup(
    name='cli-anything-postgresql',
    version='1.0.0',
    packages=['cli_anything.postgresql'],
    install_requires=['click', 'psycopg2'],
    entry_points={'console_scripts': ['cli-anything-postgresql=cli_anything.postgresql:cli']},
)
