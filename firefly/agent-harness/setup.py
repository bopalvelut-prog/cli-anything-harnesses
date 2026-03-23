from setuptools import setup
setup(
    name='cli-anything-firefly',
    version='1.0.0',
    packages=['cli_anything.firefly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-firefly=cli_anything.firefly:cli']},
)
