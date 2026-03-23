from setuptools import setup
setup(
    name='cli-anything-loan',
    version='1.0.0',
    packages=['cli_anything.loan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-loan=cli_anything.loan:cli']},
)
