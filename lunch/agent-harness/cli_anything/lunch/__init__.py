import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lunch running')
@cli.command()
def start(): click.echo('lunch started')
if __name__ == '__main__': cli()
