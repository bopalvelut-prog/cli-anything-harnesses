from setuptools import setup
setup(
    name='cli-anything-worst',
    version='1.0.0',
    packages=['cli_anything.worst'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-worst=cli_anything.worst:cli']},
)
