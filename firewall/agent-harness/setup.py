from setuptools import setup
setup(
    name='cli-anything-firewall',
    version='1.0.0',
    packages=['cli_anything.firewall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-firewall=cli_anything.firewall:cli']},
)
