from setuptools import setup
setup(
    name='cli-anything-performance',
    version='1.0.0',
    packages=['cli_anything.performance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-performance=cli_anything.performance:cli']},
)
