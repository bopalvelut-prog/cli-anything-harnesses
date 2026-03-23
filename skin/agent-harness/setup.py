from setuptools import setup
setup(
    name='cli-anything-skin',
    version='1.0.0',
    packages=['cli_anything.skin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-skin=cli_anything.skin:cli']},
)
