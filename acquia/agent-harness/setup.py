from setuptools import setup
setup(
    name='cli-anything-acquia',
    version='1.0.0',
    packages=['cli_anything.acquia'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-acquia=cli_anything.acquia:cli']},
)
