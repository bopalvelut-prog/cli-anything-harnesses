import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sword running')
@cli.command()
def start(): click.echo('sword started')
if __name__ == '__main__': cli()
