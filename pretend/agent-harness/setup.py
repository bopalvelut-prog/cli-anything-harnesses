from setuptools import setup
setup(
    name='cli-anything-pretend',
    version='1.0.0',
    packages=['cli_anything.pretend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pretend=cli_anything.pretend:cli']},
)
