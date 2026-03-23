import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rely running')
@cli.command()
def start(): click.echo('rely started')
if __name__ == '__main__': cli()
