from setuptools import setup
setup(
    name='cli-anything-circular',
    version='1.0.0',
    packages=['cli_anything.circular'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-circular=cli_anything.circular:cli']},
)
