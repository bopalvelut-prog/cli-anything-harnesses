from setuptools import setup
setup(
    name='cli-anything-talent',
    version='1.0.0',
    packages=['cli_anything.talent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-talent=cli_anything.talent:cli']},
)
