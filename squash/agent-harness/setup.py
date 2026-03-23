from setuptools import setup
setup(
    name='cli-anything-squash',
    version='1.0.0',
    packages=['cli_anything.squash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-squash=cli_anything.squash:cli']},
)
