from setuptools import setup
setup(
    name='cli-anything-symfony',
    version='1.0.0',
    packages=['cli_anything.symfony'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-symfony=cli_anything.symfony:cli']},
)
