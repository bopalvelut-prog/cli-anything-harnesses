import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('goal running')
@cli.command()
def start(): click.echo('goal started')
if __name__ == '__main__': cli()
