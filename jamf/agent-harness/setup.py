from setuptools import setup
setup(
    name='cli-anything-jamf',
    version='1.0.0',
    packages=['cli_anything.jamf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jamf=cli_anything.jamf:cli']},
)
