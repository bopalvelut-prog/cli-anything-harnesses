from setuptools import setup
setup(
    name='cli-anything-clock',
    version='1.0.0',
    packages=['cli_anything.clock'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clock=cli_anything.clock:cli']},
)
