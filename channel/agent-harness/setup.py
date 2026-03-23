from setuptools import setup
setup(
    name='cli-anything-channel',
    version='1.0.0',
    packages=['cli_anything.channel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-channel=cli_anything.channel:cli']},
)
