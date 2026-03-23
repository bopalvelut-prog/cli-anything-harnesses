from setuptools import setup
setup(
    name='cli-anything-serial',
    version='1.0.0',
    packages=['cli_anything.serial'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-serial=cli_anything.serial:cli']},
)
