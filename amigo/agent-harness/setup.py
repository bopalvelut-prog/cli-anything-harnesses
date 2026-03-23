from setuptools import setup
setup(
    name='cli-anything-amigo',
    version='1.0.0',
    packages=['cli_anything.amigo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amigo=cli_anything.amigo:cli']},
)
