from setuptools import setup
setup(
    name='cli-anything-quartz',
    version='1.0.0',
    packages=['cli_anything.quartz'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quartz=cli_anything.quartz:cli']},
)
