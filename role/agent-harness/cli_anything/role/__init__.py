import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('role running')
@cli.command()
def start(): click.echo('role started')
if __name__ == '__main__': cli()
