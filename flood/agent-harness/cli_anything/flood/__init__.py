import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flood running')
@cli.command()
def start(): click.echo('flood started')
if __name__ == '__main__': cli()
