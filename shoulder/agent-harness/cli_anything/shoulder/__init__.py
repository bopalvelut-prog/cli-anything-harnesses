import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shoulder running')
@cli.command()
def start(): click.echo('shoulder started')
if __name__ == '__main__': cli()
