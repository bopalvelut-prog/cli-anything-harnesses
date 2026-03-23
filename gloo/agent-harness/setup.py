from setuptools import setup
setup(
    name='cli-anything-gloo',
    version='1.0.0',
    packages=['cli_anything.gloo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gloo=cli_anything.gloo:cli']},
)
