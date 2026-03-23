from setuptools import setup
setup(
    name='cli-anything-reading',
    version='1.0.0',
    packages=['cli_anything.reading'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reading=cli_anything.reading:cli']},
)
