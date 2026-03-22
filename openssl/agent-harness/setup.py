from setuptools import setup
setup(
    name='cli-anything-openssl',
    version='1.0.0',
    packages=['cli_anything.openssl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openssl=cli_anything.openssl:cli']},
)
