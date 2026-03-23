from setuptools import setup
setup(
    name='cli-anything-specialist',
    version='1.0.0',
    packages=['cli_anything.specialist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-specialist=cli_anything.specialist:cli']},
)
