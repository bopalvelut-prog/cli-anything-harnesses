from setuptools import setup
setup(
    name='cli-anything-story',
    version='1.0.0',
    packages=['cli_anything.story'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-story=cli_anything.story:cli']},
)
