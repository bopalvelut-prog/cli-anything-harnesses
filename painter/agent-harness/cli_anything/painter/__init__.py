import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('painter running')
@cli.command()
def start(): click.echo('painter started')
if __name__ == '__main__': cli()
