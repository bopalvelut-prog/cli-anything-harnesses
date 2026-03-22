import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('domain')
def search(domain): subprocess.run(['theHarvester', '-d', domain, '-b', 'all'])
if __name__ == '__main__': cli()
