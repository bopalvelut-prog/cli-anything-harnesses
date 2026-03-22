from setuptools import setup
setup(
    name='cli-anything-joomla',
    version='1.0.0',
    packages=['cli_anything.joomla'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-joomla=cli_anything.joomla:cli']},
)
