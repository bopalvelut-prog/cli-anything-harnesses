from setuptools import setup
setup(
    name='cli-anything-mercury',
    version='1.0.0',
    packages=['cli_anything.mercury'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mercury=cli_anything.mercury:cli']},
)
