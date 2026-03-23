import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('conduct running')
@cli.command()
def start(): click.echo('conduct started')
if __name__ == '__main__': cli()
