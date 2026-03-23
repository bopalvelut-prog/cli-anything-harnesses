import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('perspective running')
@cli.command()
def start(): click.echo('perspective started')
if __name__ == '__main__': cli()
