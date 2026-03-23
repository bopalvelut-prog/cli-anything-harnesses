from setuptools import setup
setup(
    name='cli-anything-adsense',
    version='1.0.0',
    packages=['cli_anything.adsense'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adsense=cli_anything.adsense:cli']},
)
