from setuptools import setup
setup(
    name='cli-anything-postgrest',
    version='1.0.0',
    packages=['cli_anything.postgrest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-postgrest=cli_anything.postgrest:cli']},
)
