from setuptools import setup
setup(
    name='cli-anything-wireshark',
    version='1.0.0',
    packages=['cli_anything.wireshark'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wireshark=cli_anything.wireshark:cli']},
)
