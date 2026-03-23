from setuptools import setup
setup(
    name='cli-anything-nice',
    version='1.0.0',
    packages=['cli_anything.nice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nice=cli_anything.nice:cli']},
)
