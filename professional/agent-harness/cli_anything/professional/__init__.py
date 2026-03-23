import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('professional running')
@cli.command()
def start(): click.echo('professional started')
if __name__ == '__main__': cli()
