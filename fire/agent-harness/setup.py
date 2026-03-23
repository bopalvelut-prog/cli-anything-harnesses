from setuptools import setup
setup(
    name='cli-anything-fire',
    version='1.0.0',
    packages=['cli_anything.fire'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fire=cli_anything.fire:cli']},
)
