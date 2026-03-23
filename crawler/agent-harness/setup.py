from setuptools import setup
setup(
    name='cli-anything-crawler',
    version='1.0.0',
    packages=['cli_anything.crawler'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crawler=cli_anything.crawler:cli']},
)
