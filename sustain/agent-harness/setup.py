from setuptools import setup
setup(
    name='cli-anything-sustain',
    version='1.0.0',
    packages=['cli_anything.sustain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sustain=cli_anything.sustain:cli']},
)
