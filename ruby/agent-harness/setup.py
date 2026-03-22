from setuptools import setup
setup(
    name='cli-anything-ruby',
    version='1.0.0',
    packages=['cli_anything.ruby'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ruby=cli_anything.ruby:cli']},
)
