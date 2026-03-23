from setuptools import setup
setup(
    name='cli-anything-cast',
    version='1.0.0',
    packages=['cli_anything.cast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cast=cli_anything.cast:cli']},
)
