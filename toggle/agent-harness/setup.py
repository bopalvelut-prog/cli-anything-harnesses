from setuptools import setup
setup(
    name='cli-anything-toggle',
    version='1.0.0',
    packages=['cli_anything.toggle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-toggle=cli_anything.toggle:cli']},
)
