from setuptools import setup
setup(
    name='cli-anything-essay',
    version='1.0.0',
    packages=['cli_anything.essay'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-essay=cli_anything.essay:cli']},
)
