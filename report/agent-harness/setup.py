from setuptools import setup
setup(
    name='cli-anything-report',
    version='1.0.0',
    packages=['cli_anything.report'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-report=cli_anything.report:cli']},
)
