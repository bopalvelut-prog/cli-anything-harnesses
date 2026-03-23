from setuptools import setup
setup(
    name='cli-anything-justice',
    version='1.0.0',
    packages=['cli_anything.justice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-justice=cli_anything.justice:cli']},
)
