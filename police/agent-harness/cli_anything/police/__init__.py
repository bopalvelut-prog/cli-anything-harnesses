import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('police running')
@cli.command()
def start(): click.echo('police started')
if __name__ == '__main__': cli()
