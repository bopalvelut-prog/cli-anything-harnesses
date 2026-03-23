from setuptools import setup
setup(
    name='cli-anything-appveyor',
    version='1.0.0',
    packages=['cli_anything.appveyor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-appveyor=cli_anything.appveyor:cli']},
)
