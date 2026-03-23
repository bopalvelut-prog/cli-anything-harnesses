import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('capacity running')
@cli.command()
def start(): click.echo('capacity started')
if __name__ == '__main__': cli()
