from setuptools import setup
setup(
    name='cli-anything-cake',
    version='1.0.0',
    packages=['cli_anything.cake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cake=cli_anything.cake:cli']},
)
