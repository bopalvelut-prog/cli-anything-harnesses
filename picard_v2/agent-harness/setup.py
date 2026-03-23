from setuptools import setup
setup(
    name='cli-anything-picard_v2',
    version='1.0.0',
    packages=['cli_anything.picard_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-picard_v2=cli_anything.picard_v2:cli']},
)
