from setuptools import setup
setup(
    name='cli-anything-kritis',
    version='1.0.0',
    packages=['cli_anything.kritis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kritis=cli_anything.kritis:cli']},
)
