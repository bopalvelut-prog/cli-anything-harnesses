from setuptools import setup
setup(
    name='cli-anything-demonstrate',
    version='1.0.0',
    packages=['cli_anything.demonstrate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-demonstrate=cli_anything.demonstrate:cli']},
)
