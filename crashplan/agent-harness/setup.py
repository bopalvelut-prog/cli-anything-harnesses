from setuptools import setup
setup(
    name='cli-anything-crashplan',
    version='1.0.0',
    packages=['cli_anything.crashplan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crashplan=cli_anything.crashplan:cli']},
)
