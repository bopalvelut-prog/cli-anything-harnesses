import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ear running')
@cli.command()
def start(): click.echo('ear started')
if __name__ == '__main__': cli()
