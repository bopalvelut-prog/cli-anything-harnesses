from setuptools import setup
setup(
    name='cli-anything-cheek',
    version='1.0.0',
    packages=['cli_anything.cheek'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cheek=cli_anything.cheek:cli']},
)
