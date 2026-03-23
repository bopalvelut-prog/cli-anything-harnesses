from setuptools import setup
setup(
    name='cli-anything-wool',
    version='1.0.0',
    packages=['cli_anything.wool'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wool=cli_anything.wool:cli']},
)
