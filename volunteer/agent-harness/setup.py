from setuptools import setup
setup(
    name='cli-anything-volunteer',
    version='1.0.0',
    packages=['cli_anything.volunteer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-volunteer=cli_anything.volunteer:cli']},
)
