from setuptools import setup
setup(
    name='cli-anything-steal',
    version='1.0.0',
    packages=['cli_anything.steal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-steal=cli_anything.steal:cli']},
)
