from setuptools import setup
setup(
    name='cli-anything-voluntary',
    version='1.0.0',
    packages=['cli_anything.voluntary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-voluntary=cli_anything.voluntary:cli']},
)
