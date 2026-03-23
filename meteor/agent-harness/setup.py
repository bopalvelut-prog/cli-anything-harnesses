from setuptools import setup
setup(
    name='cli-anything-meteor',
    version='1.0.0',
    packages=['cli_anything.meteor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-meteor=cli_anything.meteor:cli']},
)
