from setuptools import setup
setup(
    name='cli-anything-procstat',
    version='1.0.0',
    packages=['cli_anything.procstat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-procstat=cli_anything.procstat:cli']},
)
