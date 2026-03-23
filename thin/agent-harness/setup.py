from setuptools import setup
setup(
    name='cli-anything-thin',
    version='1.0.0',
    packages=['cli_anything.thin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thin=cli_anything.thin:cli']},
)
