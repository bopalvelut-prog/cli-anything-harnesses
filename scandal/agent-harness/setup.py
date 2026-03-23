from setuptools import setup
setup(
    name='cli-anything-scandal',
    version='1.0.0',
    packages=['cli_anything.scandal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scandal=cli_anything.scandal:cli']},
)
