from setuptools import setup
setup(
    name='cli-anything-truly',
    version='1.0.0',
    packages=['cli_anything.truly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-truly=cli_anything.truly:cli']},
)
