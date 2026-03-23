from setuptools import setup
setup(
    name='cli-anything-glitch',
    version='1.0.0',
    packages=['cli_anything.glitch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-glitch=cli_anything.glitch:cli']},
)
