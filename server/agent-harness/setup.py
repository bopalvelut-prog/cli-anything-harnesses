from setuptools import setup
setup(
    name='cli-anything-server',
    version='1.0.0',
    packages=['cli_anything.server'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-server=cli_anything.server:cli']},
)
