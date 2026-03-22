from setuptools import setup
setup(
    name='cli-anything-cohesity',
    version='1.0.0',
    packages=['cli_anything.cohesity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cohesity=cli_anything.cohesity:cli']},
)
