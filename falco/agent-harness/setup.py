from setuptools import setup
setup(
    name='cli-anything-falco',
    version='1.0.0',
    packages=['cli_anything.falco'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-falco=cli_anything.falco:cli']},
)
