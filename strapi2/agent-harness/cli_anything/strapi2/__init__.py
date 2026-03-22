import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def develop(): subprocess.run(['strapi', 'develop'])
if __name__ == '__main__': cli()
