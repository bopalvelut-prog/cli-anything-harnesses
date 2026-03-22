from setuptools import setup
setup(
    name='cli-anything-grin',
    version='1.0.0',
    packages=['cli_anything.grin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grin=cli_anything.grin:cli']},
)
