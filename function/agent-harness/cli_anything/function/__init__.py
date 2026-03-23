import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('function running')
@cli.command()
def start(): click.echo('function started')
if __name__ == '__main__': cli()
