from setuptools import setup
setup(
    name='cli-anything-connector',
    version='1.0.0',
    packages=['cli_anything.connector'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-connector=cli_anything.connector:cli']},
)
