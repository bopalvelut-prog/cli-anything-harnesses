from setuptools import setup
setup(
    name='cli-anything-spinnaker',
    version='1.0.0',
    packages=['cli_anything.spinnaker'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spinnaker=cli_anything.spinnaker:cli']},
)
