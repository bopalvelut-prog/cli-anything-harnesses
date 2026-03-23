from setuptools import setup
setup(
    name='cli-anything-display',
    version='1.0.0',
    packages=['cli_anything.display'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-display=cli_anything.display:cli']},
)
