from setuptools import setup
setup(
    name='cli-anything-gem',
    version='1.0.0',
    packages=['cli_anything.gem'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gem=cli_anything.gem:cli']},
)
