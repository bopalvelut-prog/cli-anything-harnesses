from setuptools import setup
setup(
    name='cli-anything-uninstall',
    version='1.0.0',
    packages=['cli_anything.uninstall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-uninstall=cli_anything.uninstall:cli']},
)
