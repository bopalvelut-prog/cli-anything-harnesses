from setuptools import setup
setup(
    name='cli-anything-section',
    version='1.0.0',
    packages=['cli_anything.section'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-section=cli_anything.section:cli']},
)
