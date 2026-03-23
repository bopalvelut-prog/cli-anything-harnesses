from setuptools import setup
setup(
    name='cli-anything-thorough',
    version='1.0.0',
    packages=['cli_anything.thorough'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thorough=cli_anything.thorough:cli']},
)
