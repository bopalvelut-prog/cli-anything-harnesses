from setuptools import setup
setup(
    name='cli-anything-bigbluebutton',
    version='1.0.0',
    packages=['cli_anything.bigbluebutton'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bigbluebutton=cli_anything.bigbluebutton:cli']},
)
