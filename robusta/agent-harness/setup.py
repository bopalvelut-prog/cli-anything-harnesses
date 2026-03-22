from setuptools import setup
setup(
    name='cli-anything-robusta',
    version='1.0.0',
    packages=['cli_anything.robusta'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-robusta=cli_anything.robusta:cli']},
)
