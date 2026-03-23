from setuptools import setup
setup(
    name='cli-anything-arc',
    version='1.0.0',
    packages=['cli_anything.arc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arc=cli_anything.arc:cli']},
)
