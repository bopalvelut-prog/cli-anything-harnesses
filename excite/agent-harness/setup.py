from setuptools import setup
setup(
    name='cli-anything-excite',
    version='1.0.0',
    packages=['cli_anything.excite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-excite=cli_anything.excite:cli']},
)
