from setuptools import setup
setup(
    name='cli-anything-rubygems',
    version='1.0.0',
    packages=['cli_anything.rubygems'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rubygems=cli_anything.rubygems:cli']},
)
