from setuptools import setup
setup(
    name='cli-anything-spot_v2',
    version='1.0.0',
    packages=['cli_anything.spot_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spot_v2=cli_anything.spot_v2:cli']},
)
