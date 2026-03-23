from setuptools import setup
setup(
    name='cli-anything-stable',
    version='1.0.0',
    packages=['cli_anything.stable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stable=cli_anything.stable:cli']},
)
