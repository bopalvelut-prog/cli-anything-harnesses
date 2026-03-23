from setuptools import setup
setup(
    name='cli-anything-precise',
    version='1.0.0',
    packages=['cli_anything.precise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-precise=cli_anything.precise:cli']},
)
