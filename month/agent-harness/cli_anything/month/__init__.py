import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('month running')
@cli.command()
def start(): click.echo('month started')
if __name__ == '__main__': cli()
