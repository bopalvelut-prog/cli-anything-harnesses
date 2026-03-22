from setuptools import setup
setup(
    name='cli-anything-grype',
    version='1.0.0',
    packages=['cli_anything.grype'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grype=cli_anything.grype:cli']},
)
