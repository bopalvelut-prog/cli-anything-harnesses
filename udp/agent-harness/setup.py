from setuptools import setup
setup(
    name='cli-anything-udp',
    version='1.0.0',
    packages=['cli_anything.udp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-udp=cli_anything.udp:cli']},
)
