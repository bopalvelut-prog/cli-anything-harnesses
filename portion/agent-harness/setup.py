from setuptools import setup
setup(
    name='cli-anything-portion',
    version='1.0.0',
    packages=['cli_anything.portion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-portion=cli_anything.portion:cli']},
)
