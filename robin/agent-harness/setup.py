from setuptools import setup
setup(
    name='cli-anything-robin',
    version='1.0.0',
    packages=['cli_anything.robin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-robin=cli_anything.robin:cli']},
)
