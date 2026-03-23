from setuptools import setup
setup(
    name='cli-anything-pitch',
    version='1.0.0',
    packages=['cli_anything.pitch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pitch=cli_anything.pitch:cli']},
)
