from setuptools import setup
setup(
    name='cli-anything-brick',
    version='1.0.0',
    packages=['cli_anything.brick'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brick=cli_anything.brick:cli']},
)
