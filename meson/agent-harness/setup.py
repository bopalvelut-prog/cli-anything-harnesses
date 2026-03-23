from setuptools import setup
setup(
    name='cli-anything-meson',
    version='1.0.0',
    packages=['cli_anything.meson'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-meson=cli_anything.meson:cli']},
)
