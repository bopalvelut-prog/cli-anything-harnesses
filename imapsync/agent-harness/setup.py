from setuptools import setup
setup(
    name='cli-anything-imapsync',
    version='1.0.0',
    packages=['cli_anything.imapsync'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-imapsync=cli_anything.imapsync:cli']},
)
