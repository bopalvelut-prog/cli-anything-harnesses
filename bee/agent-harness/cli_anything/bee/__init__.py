import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bee running')
@cli.command()
def start(): click.echo('bee started')
if __name__ == '__main__': cli()
