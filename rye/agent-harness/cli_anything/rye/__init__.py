import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rye running')
@cli.command()
def start(): click.echo('rye started')
if __name__ == '__main__': cli()
