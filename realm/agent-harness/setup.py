from setuptools import setup
setup(
    name='cli-anything-realm',
    version='1.0.0',
    packages=['cli_anything.realm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-realm=cli_anything.realm:cli']},
)
