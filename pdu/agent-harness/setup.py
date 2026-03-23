from setuptools import setup
setup(
    name='cli-anything-pdu',
    version='1.0.0',
    packages=['cli_anything.pdu'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pdu=cli_anything.pdu:cli']},
)
