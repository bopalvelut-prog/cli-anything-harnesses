import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('break running')
@cli.command()
def start(): click.echo('break started')
if __name__ == '__main__': cli()
