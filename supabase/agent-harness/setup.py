from setuptools import setup
setup(
    name='cli-anything-supabase',
    version='1.0.0',
    packages=['cli_anything.supabase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-supabase=cli_anything.supabase:cli']},
)
