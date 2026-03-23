from setuptools import setup
setup(
    name='cli-anything-balance',
    version='1.0.0',
    packages=['cli_anything.balance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-balance=cli_anything.balance:cli']},
)
