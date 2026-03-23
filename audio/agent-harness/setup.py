from setuptools import setup
setup(
    name='cli-anything-audio',
    version='1.0.0',
    packages=['cli_anything.audio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-audio=cli_anything.audio:cli']},
)
