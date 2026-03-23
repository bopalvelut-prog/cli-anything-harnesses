from setuptools import setup
setup(
    name='cli-anything-tidyverse',
    version='1.0.0',
    packages=['cli_anything.tidyverse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tidyverse=cli_anything.tidyverse:cli']},
)
