from setuptools import setup
setup(
    name='cli-anything-wait',
    version='1.0.0',
    packages=['cli_anything.wait'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wait=cli_anything.wait:cli']},
)
