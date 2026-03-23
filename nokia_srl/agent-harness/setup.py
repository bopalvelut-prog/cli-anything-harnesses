from setuptools import setup
setup(
    name='cli-anything-nokia_srl',
    version='1.0.0',
    packages=['cli_anything.nokia_srl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nokia_srl=cli_anything.nokia_srl:cli']},
)
