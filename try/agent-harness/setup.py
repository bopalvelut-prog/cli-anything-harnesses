from setuptools import setup
setup(
    name='cli-anything-try',
    version='1.0.0',
    packages=['cli_anything.try'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-try=cli_anything.try:cli']},
)
