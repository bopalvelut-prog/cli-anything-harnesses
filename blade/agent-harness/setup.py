from setuptools import setup
setup(
    name='cli-anything-blade',
    version='1.0.0',
    packages=['cli_anything.blade'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blade=cli_anything.blade:cli']},
)
