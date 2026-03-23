from setuptools import setup
setup(
    name='cli-anything-injury',
    version='1.0.0',
    packages=['cli_anything.injury'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-injury=cli_anything.injury:cli']},
)
