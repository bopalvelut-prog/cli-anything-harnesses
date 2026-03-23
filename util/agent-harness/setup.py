from setuptools import setup
setup(
    name='cli-anything-util',
    version='1.0.0',
    packages=['cli_anything.util'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-util=cli_anything.util:cli']},
)
