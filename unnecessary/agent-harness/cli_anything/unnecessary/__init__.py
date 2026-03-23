import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unnecessary running')
@cli.command()
def start(): click.echo('unnecessary started')
if __name__ == '__main__': cli()
