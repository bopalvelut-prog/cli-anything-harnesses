import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('community running')
@cli.command()
def start(): click.echo('community started')
if __name__ == '__main__': cli()
