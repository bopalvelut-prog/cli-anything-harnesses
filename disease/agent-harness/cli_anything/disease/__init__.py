import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('disease running')
@cli.command()
def start(): click.echo('disease started')
if __name__ == '__main__': cli()
