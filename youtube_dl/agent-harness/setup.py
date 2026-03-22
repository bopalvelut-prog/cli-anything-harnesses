from setuptools import setup
setup(
    name='cli-anything-youtube_dl',
    version='1.0.0',
    packages=['cli_anything.youtube_dl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-youtube_dl=cli_anything.youtube_dl:cli']},
)
