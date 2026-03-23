from setuptools import setup
setup(
    name='cli-anything-socketio',
    version='1.0.0',
    packages=['cli_anything.socketio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-socketio=cli_anything.socketio:cli']},
)
