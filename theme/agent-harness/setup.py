from setuptools import setup
setup(
    name='cli-anything-theme',
    version='1.0.0',
    packages=['cli_anything.theme'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-theme=cli_anything.theme:cli']},
)
