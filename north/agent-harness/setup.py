from setuptools import setup
setup(
    name='cli-anything-north',
    version='1.0.0',
    packages=['cli_anything.north'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-north=cli_anything.north:cli']},
)
