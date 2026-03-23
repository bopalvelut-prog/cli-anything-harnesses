from setuptools import setup
setup(
    name='cli-anything-decide',
    version='1.0.0',
    packages=['cli_anything.decide'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-decide=cli_anything.decide:cli']},
)
