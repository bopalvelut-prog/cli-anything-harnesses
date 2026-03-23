from setuptools import setup
setup(
    name='cli-anything-cherokee',
    version='1.0.0',
    packages=['cli_anything.cherokee'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cherokee=cli_anything.cherokee:cli']},
)
