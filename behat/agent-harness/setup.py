from setuptools import setup
setup(
    name='cli-anything-behat',
    version='1.0.0',
    packages=['cli_anything.behat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-behat=cli_anything.behat:cli']},
)
