from setuptools import setup
setup(
    name='cli-anything-female',
    version='1.0.0',
    packages=['cli_anything.female'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-female=cli_anything.female:cli']},
)
