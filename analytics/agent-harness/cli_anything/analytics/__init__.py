import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('analytics running')
@cli.command()
def start(): click.echo('analytics started')
if __name__ == '__main__': cli()
