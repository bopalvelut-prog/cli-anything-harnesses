import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('passport running')
@cli.command()
def start(): click.echo('passport started')
if __name__ == '__main__': cli()
