from setuptools import setup
setup(
    name='cli-anything-tumble',
    version='1.0.0',
    packages=['cli_anything.tumble'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tumble=cli_anything.tumble:cli']},
)
