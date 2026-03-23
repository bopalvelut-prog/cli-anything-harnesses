from setuptools import setup
setup(
    name='cli-anything-mixer',
    version='1.0.0',
    packages=['cli_anything.mixer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mixer=cli_anything.mixer:cli']},
)
