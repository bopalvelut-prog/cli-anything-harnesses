from setuptools import setup
setup(
    name='cli-anything-countly',
    version='1.0.0',
    packages=['cli_anything.countly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-countly=cli_anything.countly:cli']},
)
