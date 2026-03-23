from setuptools import setup
setup(
    name='cli-anything-smartcard',
    version='1.0.0',
    packages=['cli_anything.smartcard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-smartcard=cli_anything.smartcard:cli']},
)
