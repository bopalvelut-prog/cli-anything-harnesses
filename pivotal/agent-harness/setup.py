from setuptools import setup
setup(
    name='cli-anything-pivotal',
    version='1.0.0',
    packages=['cli_anything.pivotal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pivotal=cli_anything.pivotal:cli']},
)
