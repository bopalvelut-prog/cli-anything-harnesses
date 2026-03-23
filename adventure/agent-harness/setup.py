from setuptools import setup
setup(
    name='cli-anything-adventure',
    version='1.0.0',
    packages=['cli_anything.adventure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adventure=cli_anything.adventure:cli']},
)
