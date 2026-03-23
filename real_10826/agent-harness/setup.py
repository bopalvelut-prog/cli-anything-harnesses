from setuptools import setup
setup(
    name='cli-anything-real_10826',
    version='1.0.0',
    packages=['cli_anything.real_10826'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_10826=cli_anything.real_10826:cli']},
)
