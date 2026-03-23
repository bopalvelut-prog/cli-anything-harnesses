from setuptools import setup
setup(
    name='cli-anything-hole',
    version='1.0.0',
    packages=['cli_anything.hole'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hole=cli_anything.hole:cli']},
)
