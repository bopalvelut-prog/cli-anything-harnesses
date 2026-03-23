from setuptools import setup
setup(
    name='cli-anything-amplitude',
    version='1.0.0',
    packages=['cli_anything.amplitude'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amplitude=cli_anything.amplitude:cli']},
)
