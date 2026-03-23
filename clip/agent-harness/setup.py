from setuptools import setup
setup(
    name='cli-anything-clip',
    version='1.0.0',
    packages=['cli_anything.clip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clip=cli_anything.clip:cli']},
)
