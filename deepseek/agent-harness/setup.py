from setuptools import setup
setup(
    name='cli-anything-deepseek',
    version='1.0.0',
    packages=['cli_anything.deepseek'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deepseek=cli_anything.deepseek:cli']},
)
