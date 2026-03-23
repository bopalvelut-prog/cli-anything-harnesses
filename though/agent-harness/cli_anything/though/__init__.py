import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('though running')
@cli.command()
def start(): click.echo('though started')
if __name__ == '__main__': cli()
