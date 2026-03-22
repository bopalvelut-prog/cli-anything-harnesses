from setuptools import setup
setup(
    name='cli-anything-maidsafe',
    version='1.0.0',
    packages=['cli_anything.maidsafe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-maidsafe=cli_anything.maidsafe:cli']},
)
