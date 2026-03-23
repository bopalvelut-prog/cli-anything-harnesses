from setuptools import setup
setup(
    name='cli-anything-socket',
    version='1.0.0',
    packages=['cli_anything.socket'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-socket=cli_anything.socket:cli']},
)
