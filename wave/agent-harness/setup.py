from setuptools import setup
setup(
    name='cli-anything-wave',
    version='1.0.0',
    packages=['cli_anything.wave'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wave=cli_anything.wave:cli']},
)
