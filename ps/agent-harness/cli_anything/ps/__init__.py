import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ps running')
@cli.command()
def start(): click.echo('ps started')
if __name__ == '__main__': cli()
