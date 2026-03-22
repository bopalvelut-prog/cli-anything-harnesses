from setuptools import setup
setup(
    name='cli-anything-discord',
    version='1.0.0',
    packages=['cli_anything.discord'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-discord=cli_anything.discord:cli']},
)
