import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rustls running')
@cli.command()
def start(): click.echo('rustls started')
if __name__ == '__main__': cli()
