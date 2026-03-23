from setuptools import setup
setup(
    name='cli-anything-script',
    version='1.0.0',
    packages=['cli_anything.script'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-script=cli_anything.script:cli']},
)
