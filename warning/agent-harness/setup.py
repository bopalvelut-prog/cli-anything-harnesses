from setuptools import setup
setup(
    name='cli-anything-warning',
    version='1.0.0',
    packages=['cli_anything.warning'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-warning=cli_anything.warning:cli']},
)
