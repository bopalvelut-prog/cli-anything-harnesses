from setuptools import setup
setup(
    name='cli-anything-manager',
    version='1.0.0',
    packages=['cli_anything.manager'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-manager=cli_anything.manager:cli']},
)
