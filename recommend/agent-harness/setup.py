from setuptools import setup
setup(
    name='cli-anything-recommend',
    version='1.0.0',
    packages=['cli_anything.recommend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-recommend=cli_anything.recommend:cli']},
)
