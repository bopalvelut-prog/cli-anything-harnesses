from setuptools import setup
setup(
    name='cli-anything-websockets',
    version='1.0.0',
    packages=['cli_anything.websockets'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-websockets=cli_anything.websockets:cli']},
)
