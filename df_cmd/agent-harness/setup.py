from setuptools import setup
setup(
    name='cli-anything-df_cmd',
    version='1.0.0',
    packages=['cli_anything.df_cmd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-df_cmd=cli_anything.df_cmd:cli']},
)
