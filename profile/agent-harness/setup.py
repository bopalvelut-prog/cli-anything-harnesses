from setuptools import setup
setup(
    name='cli-anything-profile',
    version='1.0.0',
    packages=['cli_anything.profile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-profile=cli_anything.profile:cli']},
)
