from setuptools import setup
setup(
    name='cli-anything-excellent',
    version='1.0.0',
    packages=['cli_anything.excellent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-excellent=cli_anything.excellent:cli']},
)
