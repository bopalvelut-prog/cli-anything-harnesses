from setuptools import setup
setup(
    name='cli-anything-forest',
    version='1.0.0',
    packages=['cli_anything.forest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-forest=cli_anything.forest:cli']},
)
