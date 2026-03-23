from setuptools import setup
setup(
    name='cli-anything-prior',
    version='1.0.0',
    packages=['cli_anything.prior'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prior=cli_anything.prior:cli']},
)
