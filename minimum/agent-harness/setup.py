from setuptools import setup
setup(
    name='cli-anything-minimum',
    version='1.0.0',
    packages=['cli_anything.minimum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-minimum=cli_anything.minimum:cli']},
)
