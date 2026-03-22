from setuptools import setup
setup(
    name='cli-anything-puppet',
    version='1.0.0',
    packages=['cli_anything.puppet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-puppet=cli_anything.puppet:cli']},
)
