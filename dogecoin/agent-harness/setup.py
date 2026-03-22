from setuptools import setup
setup(
    name='cli-anything-dogecoin',
    version='1.0.0',
    packages=['cli_anything.dogecoin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dogecoin=cli_anything.dogecoin:cli']},
)
