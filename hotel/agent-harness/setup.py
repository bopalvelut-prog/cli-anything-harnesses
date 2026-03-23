from setuptools import setup
setup(
    name='cli-anything-hotel',
    version='1.0.0',
    packages=['cli_anything.hotel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hotel=cli_anything.hotel:cli']},
)
