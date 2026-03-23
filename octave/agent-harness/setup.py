from setuptools import setup
setup(
    name='cli-anything-octave',
    version='1.0.0',
    packages=['cli_anything.octave'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-octave=cli_anything.octave:cli']},
)
