import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('auspice running')
@cli.command()
def start(): click.echo('auspice started')
if __name__ == '__main__': cli()
