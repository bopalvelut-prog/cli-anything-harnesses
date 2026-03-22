from setuptools import setup
setup(
    name='cli-anything-piwigo',
    version='1.0.0',
    packages=['cli_anything.piwigo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-piwigo=cli_anything.piwigo:cli']},
)
