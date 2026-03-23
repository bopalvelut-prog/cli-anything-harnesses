import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pop running')
@cli.command()
def start(): click.echo('pop started')
if __name__ == '__main__': cli()
