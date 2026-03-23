from setuptools import setup
setup(
    name='cli-anything-wobble',
    version='1.0.0',
    packages=['cli_anything.wobble'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wobble=cli_anything.wobble:cli']},
)
