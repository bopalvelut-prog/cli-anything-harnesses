from setuptools import setup
setup(
    name='cli-anything-finance',
    version='1.0.0',
    packages=['cli_anything.finance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-finance=cli_anything.finance:cli']},
)
