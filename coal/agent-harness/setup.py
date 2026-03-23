from setuptools import setup
setup(
    name='cli-anything-coal',
    version='1.0.0',
    packages=['cli_anything.coal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coal=cli_anything.coal:cli']},
)
