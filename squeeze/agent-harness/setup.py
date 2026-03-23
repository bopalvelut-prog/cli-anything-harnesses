from setuptools import setup
setup(
    name='cli-anything-squeeze',
    version='1.0.0',
    packages=['cli_anything.squeeze'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-squeeze=cli_anything.squeeze:cli']},
)
