from setuptools import setup
setup(
    name='cli-anything-bridgecrew',
    version='1.0.0',
    packages=['cli_anything.bridgecrew'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bridgecrew=cli_anything.bridgecrew:cli']},
)
