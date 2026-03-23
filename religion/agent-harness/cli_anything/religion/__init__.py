import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('religion running')
@cli.command()
def start(): click.echo('religion started')
if __name__ == '__main__': cli()
