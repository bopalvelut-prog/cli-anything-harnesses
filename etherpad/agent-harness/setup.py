from setuptools import setup
setup(
    name='cli-anything-etherpad',
    version='1.0.0',
    packages=['cli_anything.etherpad'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-etherpad=cli_anything.etherpad:cli']},
)
