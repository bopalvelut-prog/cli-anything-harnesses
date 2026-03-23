from setuptools import setup
setup(
    name='cli-anything-context',
    version='1.0.0',
    packages=['cli_anything.context'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-context=cli_anything.context:cli']},
)
