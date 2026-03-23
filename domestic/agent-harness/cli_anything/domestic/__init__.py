import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('domestic running')
@cli.command()
def start(): click.echo('domestic started')
if __name__ == '__main__': cli()
