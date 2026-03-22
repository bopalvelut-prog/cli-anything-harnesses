from setuptools import setup
setup(
    name='cli-anything-fortify',
    version='1.0.0',
    packages=['cli_anything.fortify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fortify=cli_anything.fortify:cli']},
)
