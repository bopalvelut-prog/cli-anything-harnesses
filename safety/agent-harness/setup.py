from setuptools import setup
setup(
    name='cli-anything-safety',
    version='1.0.0',
    packages=['cli_anything.safety'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-safety=cli_anything.safety:cli']},
)
