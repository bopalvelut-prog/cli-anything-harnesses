import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stranger running')
@cli.command()
def start(): click.echo('stranger started')
if __name__ == '__main__': cli()
