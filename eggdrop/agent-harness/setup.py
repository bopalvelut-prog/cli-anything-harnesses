from setuptools import setup
setup(
    name='cli-anything-eggdrop',
    version='1.0.0',
    packages=['cli_anything.eggdrop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-eggdrop=cli_anything.eggdrop:cli']},
)
