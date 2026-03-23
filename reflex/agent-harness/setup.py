from setuptools import setup
setup(
    name='cli-anything-reflex',
    version='1.0.0',
    packages=['cli_anything.reflex'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reflex=cli_anything.reflex:cli']},
)
