import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('water running')
@cli.command()
def start(): click.echo('water started')
if __name__ == '__main__': cli()
