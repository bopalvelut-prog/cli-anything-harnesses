import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rebuild running')
@cli.command()
def start(): click.echo('rebuild started')
if __name__ == '__main__': cli()
