from setuptools import setup
setup(
    name='cli-anything-unsloth',
    version='1.0.0',
    packages=['cli_anything.unsloth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unsloth=cli_anything.unsloth:cli']},
)
