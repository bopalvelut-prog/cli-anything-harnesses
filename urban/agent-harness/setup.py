from setuptools import setup
setup(
    name='cli-anything-urban',
    version='1.0.0',
    packages=['cli_anything.urban'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-urban=cli_anything.urban:cli']},
)
