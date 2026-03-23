from setuptools import setup
setup(
    name='cli-anything-ctop',
    version='1.0.0',
    packages=['cli_anything.ctop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ctop=cli_anything.ctop:cli']},
)
