from setuptools import setup
setup(
    name='cli-anything-techno',
    version='1.0.0',
    packages=['cli_anything.techno'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-techno=cli_anything.techno:cli']},
)
