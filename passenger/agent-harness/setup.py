from setuptools import setup
setup(
    name='cli-anything-passenger',
    version='1.0.0',
    packages=['cli_anything.passenger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-passenger=cli_anything.passenger:cli']},
)
