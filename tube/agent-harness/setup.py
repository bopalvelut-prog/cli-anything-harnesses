from setuptools import setup
setup(
    name='cli-anything-tube',
    version='1.0.0',
    packages=['cli_anything.tube'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tube=cli_anything.tube:cli']},
)
