from setuptools import setup
setup(
    name='cli-anything-nmap',
    version='1.0.0',
    packages=['cli_anything.nmap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nmap=cli_anything.nmap:cli']},
)
