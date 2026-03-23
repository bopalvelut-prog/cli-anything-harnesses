from setuptools import setup
setup(
    name='cli-anything-boto',
    version='1.0.0',
    packages=['cli_anything.boto'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-boto=cli_anything.boto:cli']},
)
