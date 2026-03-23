from setuptools import setup
setup(
    name='cli-anything-kde',
    version='1.0.0',
    packages=['cli_anything.kde'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kde=cli_anything.kde:cli']},
)
