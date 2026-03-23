import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dress running')
@cli.command()
def start(): click.echo('dress started')
if __name__ == '__main__': cli()
