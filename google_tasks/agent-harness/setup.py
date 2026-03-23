from setuptools import setup
setup(
    name='cli-anything-google_tasks',
    version='1.0.0',
    packages=['cli_anything.google_tasks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-google_tasks=cli_anything.google_tasks:cli']},
)
