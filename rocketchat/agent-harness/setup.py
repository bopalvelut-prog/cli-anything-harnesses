from setuptools import setup
setup(
    name='cli-anything-rocketchat',
    version='1.0.0',
    packages=['cli_anything.rocketchat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rocketchat=cli_anything.rocketchat:cli']},
)
