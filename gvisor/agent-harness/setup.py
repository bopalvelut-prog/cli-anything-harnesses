from setuptools import setup
setup(
    name='cli-anything-gvisor',
    version='1.0.0',
    packages=['cli_anything.gvisor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gvisor=cli_anything.gvisor:cli']},
)
