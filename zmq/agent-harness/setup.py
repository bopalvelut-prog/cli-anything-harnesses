from setuptools import setup
setup(
    name='cli-anything-zmq',
    version='1.0.0',
    packages=['cli_anything.zmq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zmq=cli_anything.zmq:cli']},
)
