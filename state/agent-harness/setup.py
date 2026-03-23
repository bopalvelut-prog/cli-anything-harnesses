from setuptools import setup
setup(
    name='cli-anything-state',
    version='1.0.0',
    packages=['cli_anything.state'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-state=cli_anything.state:cli']},
)
