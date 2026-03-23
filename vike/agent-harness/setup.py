from setuptools import setup
setup(
    name='cli-anything-vike',
    version='1.0.0',
    packages=['cli_anything.vike'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vike=cli_anything.vike:cli']},
)
