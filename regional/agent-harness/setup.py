from setuptools import setup
setup(
    name='cli-anything-regional',
    version='1.0.0',
    packages=['cli_anything.regional'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-regional=cli_anything.regional:cli']},
)
