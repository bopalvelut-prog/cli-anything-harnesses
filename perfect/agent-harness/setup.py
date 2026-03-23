from setuptools import setup
setup(
    name='cli-anything-perfect',
    version='1.0.0',
    packages=['cli_anything.perfect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-perfect=cli_anything.perfect:cli']},
)
