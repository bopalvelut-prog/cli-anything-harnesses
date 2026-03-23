from setuptools import setup
setup(
    name='cli-anything-net',
    version='1.0.0',
    packages=['cli_anything.net'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-net=cli_anything.net:cli']},
)
