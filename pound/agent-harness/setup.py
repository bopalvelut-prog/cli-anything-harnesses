from setuptools import setup
setup(
    name='cli-anything-pound',
    version='1.0.0',
    packages=['cli_anything.pound'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pound=cli_anything.pound:cli']},
)
