from setuptools import setup
setup(
    name='cli-anything-repeat',
    version='1.0.0',
    packages=['cli_anything.repeat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-repeat=cli_anything.repeat:cli']},
)
