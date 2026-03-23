from setuptools import setup
setup(
    name='cli-anything-receive',
    version='1.0.0',
    packages=['cli_anything.receive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-receive=cli_anything.receive:cli']},
)
