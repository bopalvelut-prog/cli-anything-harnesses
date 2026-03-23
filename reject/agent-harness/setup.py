from setuptools import setup
setup(
    name='cli-anything-reject',
    version='1.0.0',
    packages=['cli_anything.reject'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reject=cli_anything.reject:cli']},
)
