from setuptools import setup
setup(
    name='cli-anything-tenure',
    version='1.0.0',
    packages=['cli_anything.tenure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tenure=cli_anything.tenure:cli']},
)
