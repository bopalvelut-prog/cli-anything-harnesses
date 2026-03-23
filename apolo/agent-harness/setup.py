from setuptools import setup
setup(
    name='cli-anything-apolo',
    version='1.0.0',
    packages=['cli_anything.apolo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apolo=cli_anything.apolo:cli']},
)
