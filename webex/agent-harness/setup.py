from setuptools import setup
setup(
    name='cli-anything-webex',
    version='1.0.0',
    packages=['cli_anything.webex'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-webex=cli_anything.webex:cli']},
)
