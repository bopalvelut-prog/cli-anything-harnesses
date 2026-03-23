import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pica running')
@cli.command()
def start(): click.echo('pica started')
if __name__ == '__main__': cli()
