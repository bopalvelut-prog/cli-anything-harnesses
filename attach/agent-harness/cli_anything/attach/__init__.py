import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('attach running')
@cli.command()
def start(): click.echo('attach started')
if __name__ == '__main__': cli()
