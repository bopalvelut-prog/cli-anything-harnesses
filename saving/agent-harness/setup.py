from setuptools import setup
setup(
    name='cli-anything-saving',
    version='1.0.0',
    packages=['cli_anything.saving'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-saving=cli_anything.saving:cli']},
)
