from setuptools import setup
setup(
    name='cli-anything-smash',
    version='1.0.0',
    packages=['cli_anything.smash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-smash=cli_anything.smash:cli']},
)
