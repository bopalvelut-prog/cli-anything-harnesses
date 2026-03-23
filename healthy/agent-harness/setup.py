from setuptools import setup
setup(
    name='cli-anything-healthy',
    version='1.0.0',
    packages=['cli_anything.healthy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-healthy=cli_anything.healthy:cli']},
)
