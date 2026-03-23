from setuptools import setup
setup(
    name='cli-anything-pyxel',
    version='1.0.0',
    packages=['cli_anything.pyxel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pyxel=cli_anything.pyxel:cli']},
)
