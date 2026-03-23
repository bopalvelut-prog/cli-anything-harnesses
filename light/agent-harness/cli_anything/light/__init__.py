import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('light running')
@cli.command()
def start(): click.echo('light started')
if __name__ == '__main__': cli()
