from setuptools import setup
setup(
    name='cli-anything-hashcat',
    version='1.0.0',
    packages=['cli_anything.hashcat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hashcat=cli_anything.hashcat:cli']},
)
