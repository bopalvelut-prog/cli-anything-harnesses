from setuptools import setup
setup(
    name='cli-anything-lay',
    version='1.0.0',
    packages=['cli_anything.lay'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lay=cli_anything.lay:cli']},
)
