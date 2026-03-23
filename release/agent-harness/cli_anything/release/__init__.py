import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('release running')
@cli.command()
def start(): click.echo('release started')
if __name__ == '__main__': cli()
