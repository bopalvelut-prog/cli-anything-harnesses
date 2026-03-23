from setuptools import setup
setup(
    name='cli-anything-chocolate',
    version='1.0.0',
    packages=['cli_anything.chocolate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chocolate=cli_anything.chocolate:cli']},
)
