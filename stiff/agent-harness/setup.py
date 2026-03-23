from setuptools import setup
setup(
    name='cli-anything-stiff',
    version='1.0.0',
    packages=['cli_anything.stiff'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stiff=cli_anything.stiff:cli']},
)
