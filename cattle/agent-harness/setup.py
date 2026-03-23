from setuptools import setup
setup(
    name='cli-anything-cattle',
    version='1.0.0',
    packages=['cli_anything.cattle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cattle=cli_anything.cattle:cli']},
)
