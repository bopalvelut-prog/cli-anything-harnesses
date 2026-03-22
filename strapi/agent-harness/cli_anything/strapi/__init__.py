import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def develop(): subprocess.run(['strapi', 'develop'])
@cli.command()
def build(): subprocess.run(['strapi', 'build'])
@cli.command()
def start(): subprocess.run(['strapi', 'start'])
if __name__ == '__main__': cli()
