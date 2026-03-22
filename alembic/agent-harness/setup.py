from setuptools import setup
setup(
    name='cli-anything-alembic',
    version='1.0.0',
    packages=['cli_anything.alembic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alembic=cli_anything.alembic:cli']},
)
