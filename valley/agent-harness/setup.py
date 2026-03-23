from setuptools import setup
setup(
    name='cli-anything-valley',
    version='1.0.0',
    packages=['cli_anything.valley'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-valley=cli_anything.valley:cli']},
)
