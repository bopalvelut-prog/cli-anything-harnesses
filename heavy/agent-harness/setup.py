from setuptools import setup
setup(
    name='cli-anything-heavy',
    version='1.0.0',
    packages=['cli_anything.heavy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-heavy=cli_anything.heavy:cli']},
)
