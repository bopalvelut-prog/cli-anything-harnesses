from setuptools import setup
setup(
    name='cli-anything-gandi_v2',
    version='1.0.0',
    packages=['cli_anything.gandi_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gandi_v2=cli_anything.gandi_v2:cli']},
)
