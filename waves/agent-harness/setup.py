from setuptools import setup
setup(
    name='cli-anything-waves',
    version='1.0.0',
    packages=['cli_anything.waves'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-waves=cli_anything.waves:cli']},
)
