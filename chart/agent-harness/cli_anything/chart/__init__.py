import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chart running')
@cli.command()
def start(): click.echo('chart started')
if __name__ == '__main__': cli()
