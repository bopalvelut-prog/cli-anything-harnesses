from setuptools import setup
setup(
    name='cli-anything-slightly',
    version='1.0.0',
    packages=['cli_anything.slightly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slightly=cli_anything.slightly:cli']},
)
