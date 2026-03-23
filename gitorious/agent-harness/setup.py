from setuptools import setup
setup(
    name='cli-anything-gitorious',
    version='1.0.0',
    packages=['cli_anything.gitorious'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gitorious=cli_anything.gitorious:cli']},
)
