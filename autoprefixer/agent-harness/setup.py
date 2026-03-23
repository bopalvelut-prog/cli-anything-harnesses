from setuptools import setup
setup(
    name='cli-anything-autoprefixer',
    version='1.0.0',
    packages=['cli_anything.autoprefixer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autoprefixer=cli_anything.autoprefixer:cli']},
)
