from setuptools import setup
setup(
    name='cli-anything-rubocop',
    version='1.0.0',
    packages=['cli_anything.rubocop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rubocop=cli_anything.rubocop:cli']},
)
