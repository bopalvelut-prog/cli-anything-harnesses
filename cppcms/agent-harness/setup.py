from setuptools import setup
setup(
    name='cli-anything-cppcms',
    version='1.0.0',
    packages=['cli_anything.cppcms'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cppcms=cli_anything.cppcms:cli']},
)
