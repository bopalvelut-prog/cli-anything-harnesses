from setuptools import setup
setup(
    name='cli-anything-apprise',
    version='1.0.0',
    packages=['cli_anything.apprise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apprise=cli_anything.apprise:cli']},
)
