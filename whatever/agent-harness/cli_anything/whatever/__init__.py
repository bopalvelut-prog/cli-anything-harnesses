import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('whatever running')
@cli.command()
def start(): click.echo('whatever started')
if __name__ == '__main__': cli()
