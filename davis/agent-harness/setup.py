from setuptools import setup
setup(
    name='cli-anything-davis',
    version='1.0.0',
    packages=['cli_anything.davis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-davis=cli_anything.davis:cli']},
)
