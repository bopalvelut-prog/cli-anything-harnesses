from setuptools import setup
setup(
    name='cli-anything-inch',
    version='1.0.0',
    packages=['cli_anything.inch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-inch=cli_anything.inch:cli']},
)
