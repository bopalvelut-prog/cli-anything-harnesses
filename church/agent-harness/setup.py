from setuptools import setup
setup(
    name='cli-anything-church',
    version='1.0.0',
    packages=['cli_anything.church'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-church=cli_anything.church:cli']},
)
