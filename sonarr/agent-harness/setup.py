from setuptools import setup
setup(
    name='cli-anything-sonarr',
    version='1.0.0',
    packages=['cli_anything.sonarr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sonarr=cli_anything.sonarr:cli']},
)
