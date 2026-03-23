from setuptools import setup
setup(
    name='cli-anything-pump',
    version='1.0.0',
    packages=['cli_anything.pump'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pump=cli_anything.pump:cli']},
)
