from setuptools import setup
setup(
    name='cli-anything-tooth',
    version='1.0.0',
    packages=['cli_anything.tooth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tooth=cli_anything.tooth:cli']},
)
