from setuptools import setup
setup(
    name='cli-anything-regulation',
    version='1.0.0',
    packages=['cli_anything.regulation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-regulation=cli_anything.regulation:cli']},
)
