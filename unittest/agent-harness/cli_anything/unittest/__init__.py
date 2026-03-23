import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unittest running')
@cli.command()
def start(): click.echo('unittest started')
if __name__ == '__main__': cli()
