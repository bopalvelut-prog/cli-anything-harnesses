from setuptools import setup
setup(
    name='cli-anything-romana',
    version='1.0.0',
    packages=['cli_anything.romana'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-romana=cli_anything.romana:cli']},
)
