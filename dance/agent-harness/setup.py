from setuptools import setup
setup(
    name='cli-anything-dance',
    version='1.0.0',
    packages=['cli_anything.dance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dance=cli_anything.dance:cli']},
)
