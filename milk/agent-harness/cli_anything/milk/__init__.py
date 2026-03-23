import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('milk running')
@cli.command()
def start(): click.echo('milk started')
if __name__ == '__main__': cli()
