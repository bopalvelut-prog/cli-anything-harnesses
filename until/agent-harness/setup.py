from setuptools import setup
setup(
    name='cli-anything-until',
    version='1.0.0',
    packages=['cli_anything.until'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-until=cli_anything.until:cli']},
)
