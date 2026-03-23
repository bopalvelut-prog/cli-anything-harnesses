from setuptools import setup
setup(
    name='cli-anything-roadmap',
    version='1.0.0',
    packages=['cli_anything.roadmap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-roadmap=cli_anything.roadmap:cli']},
)
