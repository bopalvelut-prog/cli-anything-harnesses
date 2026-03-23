from setuptools import setup
setup(
    name='cli-anything-ginger',
    version='1.0.0',
    packages=['cli_anything.ginger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ginger=cli_anything.ginger:cli']},
)
