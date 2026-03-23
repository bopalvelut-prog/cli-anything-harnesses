from setuptools import setup
setup(
    name='cli-anything-mp3',
    version='1.0.0',
    packages=['cli_anything.mp3'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mp3=cli_anything.mp3:cli']},
)
