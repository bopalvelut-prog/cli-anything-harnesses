from setuptools import setup
setup(
    name='cli-anything-jooq',
    version='1.0.0',
    packages=['cli_anything.jooq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jooq=cli_anything.jooq:cli']},
)
