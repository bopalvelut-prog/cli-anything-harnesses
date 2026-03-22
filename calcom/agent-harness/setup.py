from setuptools import setup
setup(
    name='cli-anything-calcom',
    version='1.0.0',
    packages=['cli_anything.calcom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-calcom=cli_anything.calcom:cli']},
)
