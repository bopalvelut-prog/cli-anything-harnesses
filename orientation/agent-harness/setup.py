from setuptools import setup
setup(
    name='cli-anything-orientation',
    version='1.0.0',
    packages=['cli_anything.orientation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-orientation=cli_anything.orientation:cli']},
)
