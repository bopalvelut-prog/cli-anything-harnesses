from setuptools import setup
setup(
    name='cli-anything-lift',
    version='1.0.0',
    packages=['cli_anything.lift'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lift=cli_anything.lift:cli']},
)
