from setuptools import setup
setup(
    name='cli-anything-scikit',
    version='1.0.0',
    packages=['cli_anything.scikit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scikit=cli_anything.scikit:cli']},
)
