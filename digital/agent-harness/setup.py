from setuptools import setup
setup(
    name='cli-anything-digital',
    version='1.0.0',
    packages=['cli_anything.digital'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-digital=cli_anything.digital:cli']},
)
