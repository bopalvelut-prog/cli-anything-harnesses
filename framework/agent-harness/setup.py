from setuptools import setup
setup(
    name='cli-anything-framework',
    version='1.0.0',
    packages=['cli_anything.framework'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-framework=cli_anything.framework:cli']},
)
