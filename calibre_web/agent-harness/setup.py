from setuptools import setup
setup(
    name='cli-anything-calibre_web',
    version='1.0.0',
    packages=['cli_anything.calibre_web'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-calibre_web=cli_anything.calibre_web:cli']},
)
