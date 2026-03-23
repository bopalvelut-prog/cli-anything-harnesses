from setuptools import setup
setup(
    name='cli-anything-dramatic',
    version='1.0.0',
    packages=['cli_anything.dramatic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dramatic=cli_anything.dramatic:cli']},
)
