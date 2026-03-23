from setuptools import setup
setup(
    name='cli-anything-avd',
    version='1.0.0',
    packages=['cli_anything.avd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-avd=cli_anything.avd:cli']},
)
