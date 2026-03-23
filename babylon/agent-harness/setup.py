from setuptools import setup
setup(
    name='cli-anything-babylon',
    version='1.0.0',
    packages=['cli_anything.babylon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-babylon=cli_anything.babylon:cli']},
)
