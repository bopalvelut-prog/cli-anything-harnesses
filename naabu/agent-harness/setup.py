from setuptools import setup
setup(
    name='cli-anything-naabu',
    version='1.0.0',
    packages=['cli_anything.naabu'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-naabu=cli_anything.naabu:cli']},
)
