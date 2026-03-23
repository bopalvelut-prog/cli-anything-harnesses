import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ciao running')
@cli.command()
def start(): click.echo('ciao started')
if __name__ == '__main__': cli()
