from setuptools import setup
setup(
    name='cli-anything-tower',
    version='1.0.0',
    packages=['cli_anything.tower'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tower=cli_anything.tower:cli']},
)
