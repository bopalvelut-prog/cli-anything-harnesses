from setuptools import setup
setup(
    name='cli-anything-trunk',
    version='1.0.0',
    packages=['cli_anything.trunk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trunk=cli_anything.trunk:cli']},
)
