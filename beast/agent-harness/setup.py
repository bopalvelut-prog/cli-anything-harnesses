from setuptools import setup
setup(
    name='cli-anything-beast',
    version='1.0.0',
    packages=['cli_anything.beast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beast=cli_anything.beast:cli']},
)
