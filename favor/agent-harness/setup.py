from setuptools import setup
setup(
    name='cli-anything-favor',
    version='1.0.0',
    packages=['cli_anything.favor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-favor=cli_anything.favor:cli']},
)
