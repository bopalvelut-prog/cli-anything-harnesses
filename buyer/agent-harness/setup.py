from setuptools import setup
setup(
    name='cli-anything-buyer',
    version='1.0.0',
    packages=['cli_anything.buyer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-buyer=cli_anything.buyer:cli']},
)
