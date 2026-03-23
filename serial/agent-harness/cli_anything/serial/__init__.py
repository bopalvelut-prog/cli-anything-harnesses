import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('serial running')
@cli.command()
def start(): click.echo('serial started')
if __name__ == '__main__': cli()
