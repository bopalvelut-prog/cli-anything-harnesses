import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('token running')
@cli.command()
def start(): click.echo('token started')
if __name__ == '__main__': cli()
