from setuptools import setup
setup(
    name='cli-anything-metasploit',
    version='1.0.0',
    packages=['cli_anything.metasploit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-metasploit=cli_anything.metasploit:cli']},
)
