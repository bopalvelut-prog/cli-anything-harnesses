from setuptools import setup
setup(
    name='cli-anything-cypress',
    version='1.0.0',
    packages=['cli_anything.cypress'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cypress=cli_anything.cypress:cli']},
)
