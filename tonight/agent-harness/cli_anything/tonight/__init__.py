import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tonight running')
@cli.command()
def start(): click.echo('tonight started')
if __name__ == '__main__': cli()
