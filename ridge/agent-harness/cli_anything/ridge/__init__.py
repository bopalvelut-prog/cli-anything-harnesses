import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ridge running')
@cli.command()
def start(): click.echo('ridge started')
if __name__ == '__main__': cli()
