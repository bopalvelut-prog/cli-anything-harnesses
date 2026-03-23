from setuptools import setup
setup(
    name='cli-anything-decline',
    version='1.0.0',
    packages=['cli_anything.decline'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-decline=cli_anything.decline:cli']},
)
