import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spin running')
@cli.command()
def start(): click.echo('spin started')
if __name__ == '__main__': cli()
