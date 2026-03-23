import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('resin running')
@cli.command()
def start(): click.echo('resin started')
if __name__ == '__main__': cli()
