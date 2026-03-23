from setuptools import setup
setup(
    name='cli-anything-meeting',
    version='1.0.0',
    packages=['cli_anything.meeting'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-meeting=cli_anything.meeting:cli']},
)
