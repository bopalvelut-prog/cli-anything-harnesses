from setuptools import setup
setup(
    name='cli-anything-sound',
    version='1.0.0',
    packages=['cli_anything.sound'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sound=cli_anything.sound:cli']},
)
