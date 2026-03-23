from setuptools import setup
setup(
    name='cli-anything-rainbow',
    version='1.0.0',
    packages=['cli_anything.rainbow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rainbow=cli_anything.rainbow:cli']},
)
