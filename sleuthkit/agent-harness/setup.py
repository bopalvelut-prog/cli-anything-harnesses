from setuptools import setup
setup(
    name='cli-anything-sleuthkit',
    version='1.0.0',
    packages=['cli_anything.sleuthkit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sleuthkit=cli_anything.sleuthkit:cli']},
)
