from setuptools import setup
setup(
    name='cli-anything-lacework',
    version='1.0.0',
    packages=['cli_anything.lacework'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lacework=cli_anything.lacework:cli']},
)
