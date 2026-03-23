import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('either running')
@cli.command()
def start(): click.echo('either started')
if __name__ == '__main__': cli()
