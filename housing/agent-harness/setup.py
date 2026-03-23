from setuptools import setup
setup(
    name='cli-anything-housing',
    version='1.0.0',
    packages=['cli_anything.housing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-housing=cli_anything.housing:cli']},
)
