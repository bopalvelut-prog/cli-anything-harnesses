from setuptools import setup
setup(
    name='cli-anything-kamon',
    version='1.0.0',
    packages=['cli_anything.kamon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kamon=cli_anything.kamon:cli']},
)
