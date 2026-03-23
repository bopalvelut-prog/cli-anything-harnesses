import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('whether running')
@cli.command()
def start(): click.echo('whether started')
if __name__ == '__main__': cli()
