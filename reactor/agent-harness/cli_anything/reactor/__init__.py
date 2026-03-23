import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reactor running')
@cli.command()
def start(): click.echo('reactor started')
if __name__ == '__main__': cli()
