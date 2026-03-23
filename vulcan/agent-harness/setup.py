from setuptools import setup
setup(
    name='cli-anything-vulcan',
    version='1.0.0',
    packages=['cli_anything.vulcan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vulcan=cli_anything.vulcan:cli']},
)
