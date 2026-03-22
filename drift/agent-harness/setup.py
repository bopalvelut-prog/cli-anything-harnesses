from setuptools import setup
setup(
    name='cli-anything-drift',
    version='1.0.0',
    packages=['cli_anything.drift'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drift=cli_anything.drift:cli']},
)
