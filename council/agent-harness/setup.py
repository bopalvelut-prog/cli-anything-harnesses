from setuptools import setup
setup(
    name='cli-anything-council',
    version='1.0.0',
    packages=['cli_anything.council'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-council=cli_anything.council:cli']},
)
