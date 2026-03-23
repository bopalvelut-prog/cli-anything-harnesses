from setuptools import setup
setup(
    name='cli-anything-speak',
    version='1.0.0',
    packages=['cli_anything.speak'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-speak=cli_anything.speak:cli']},
)
