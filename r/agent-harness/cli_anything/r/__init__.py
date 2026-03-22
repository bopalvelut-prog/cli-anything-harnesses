import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('script')
def run(script): subprocess.run(['Rscript', script])
@cli.command()
def shell(): subprocess.run(['R'])
@cli.command()
def install(): subprocess.run(['R', '-e', "install.packages('tidyverse')"])
if __name__ == '__main__': cli()
