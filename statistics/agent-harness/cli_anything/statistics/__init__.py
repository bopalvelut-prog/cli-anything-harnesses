import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('statistics running')
@cli.command()
def start(): click.echo('statistics started')
if __name__ == '__main__': cli()
