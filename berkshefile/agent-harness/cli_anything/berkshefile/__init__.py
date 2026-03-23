import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('berkshefile running')
@cli.command()
def start(): click.echo('berkshefile started')
if __name__ == '__main__': cli()
