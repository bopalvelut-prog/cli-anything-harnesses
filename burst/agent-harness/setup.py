from setuptools import setup
setup(
    name='cli-anything-burst',
    version='1.0.0',
    packages=['cli_anything.burst'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-burst=cli_anything.burst:cli']},
)
