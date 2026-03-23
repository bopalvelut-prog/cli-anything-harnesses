from setuptools import setup
setup(
    name='cli-anything-protest',
    version='1.0.0',
    packages=['cli_anything.protest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-protest=cli_anything.protest:cli']},
)
