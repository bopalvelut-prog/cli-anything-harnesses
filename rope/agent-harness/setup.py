from setuptools import setup
setup(
    name='cli-anything-rope',
    version='1.0.0',
    packages=['cli_anything.rope'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rope=cli_anything.rope:cli']},
)
