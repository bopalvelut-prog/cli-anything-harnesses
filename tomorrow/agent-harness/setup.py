from setuptools import setup
setup(
    name='cli-anything-tomorrow',
    version='1.0.0',
    packages=['cli_anything.tomorrow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tomorrow=cli_anything.tomorrow:cli']},
)
