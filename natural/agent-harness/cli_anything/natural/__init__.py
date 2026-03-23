import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('natural running')
@cli.command()
def start(): click.echo('natural started')
if __name__ == '__main__': cli()
