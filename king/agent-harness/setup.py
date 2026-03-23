from setuptools import setup
setup(
    name='cli-anything-king',
    version='1.0.0',
    packages=['cli_anything.king'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-king=cli_anything.king:cli']},
)
