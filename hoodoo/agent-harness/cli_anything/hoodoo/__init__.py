import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hoodoo running')
@cli.command()
def start(): click.echo('hoodoo started')
if __name__ == '__main__': cli()
