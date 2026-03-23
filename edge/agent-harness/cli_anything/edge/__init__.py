import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('edge running')
@cli.command()
def start(): click.echo('edge started')
if __name__ == '__main__': cli()
