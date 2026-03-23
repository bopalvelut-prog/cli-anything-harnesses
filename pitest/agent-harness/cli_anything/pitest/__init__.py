import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pitest running')
@cli.command()
def start(): click.echo('pitest started')
if __name__ == '__main__': cli()
