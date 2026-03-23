from setuptools import setup
setup(
    name='cli-anything-vhs',
    version='1.0.0',
    packages=['cli_anything.vhs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vhs=cli_anything.vhs:cli']},
)
