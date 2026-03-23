from setuptools import setup
setup(
    name='cli-anything-moment',
    version='1.0.0',
    packages=['cli_anything.moment'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-moment=cli_anything.moment:cli']},
)
