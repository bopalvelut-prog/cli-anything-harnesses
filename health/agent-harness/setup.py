from setuptools import setup
setup(
    name='cli-anything-health',
    version='1.0.0',
    packages=['cli_anything.health'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-health=cli_anything.health:cli']},
)
