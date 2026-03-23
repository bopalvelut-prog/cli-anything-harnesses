from setuptools import setup
setup(
    name='cli-anything-postcss',
    version='1.0.0',
    packages=['cli_anything.postcss'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-postcss=cli_anything.postcss:cli']},
)
