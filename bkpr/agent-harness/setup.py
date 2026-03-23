from setuptools import setup
setup(
    name='cli-anything-bkpr',
    version='1.0.0',
    packages=['cli_anything.bkpr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bkpr=cli_anything.bkpr:cli']},
)
