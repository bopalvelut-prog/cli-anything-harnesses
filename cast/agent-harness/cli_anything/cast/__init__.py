import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cast running')
@cli.command()
def start(): click.echo('cast started')
if __name__ == '__main__': cli()
