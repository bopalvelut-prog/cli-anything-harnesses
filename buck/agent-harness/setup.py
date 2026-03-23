from setuptools import setup
setup(
    name='cli-anything-buck',
    version='1.0.0',
    packages=['cli_anything.buck'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-buck=cli_anything.buck:cli']},
)
