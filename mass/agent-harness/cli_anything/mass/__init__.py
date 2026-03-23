import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mass running')
@cli.command()
def start(): click.echo('mass started')
if __name__ == '__main__': cli()
