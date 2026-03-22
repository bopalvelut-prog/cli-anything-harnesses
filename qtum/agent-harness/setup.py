from setuptools import setup
setup(
    name='cli-anything-qtum',
    version='1.0.0',
    packages=['cli_anything.qtum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-qtum=cli_anything.qtum:cli']},
)
